import logging
import uuid

import b2c2_api
from b2c2_api.rest import ApiException
from b2c2_api.models import OrderRequest, QuoteRequest

import click

logger = logging.getLogger(__name__)


@click.group()
@click.option("--log-level", envvar="LOG_LEVEL", default="INFO")
@click.option("--host", envvar="HOST", default="https://api.uat.b2c2.net")
@click.option("--token", envvar="TOKEN")
@click.version_option()
@click.pass_context
def cli(ctx, log_level, host, token):
    logger.setLevel(logging.getLevelName(log_level))
    logger.debug(f"host: {host}")
    logger.debug(f"token: {token}")
    configuration = b2c2_api.Configuration(
        host=host, api_key=token  # TODO align terminology token vs api_key
    )
    ctx.obj = {"configuration": configuration}
    """The B2C2 CLI provides developers with 24x7 programmatic access to B2C2 cryptocurrencies trading backend."""


@cli.command()
@click.pass_context
def balances(ctx):
    """Get Balances."""
    configuration = ctx.obj["configuration"]
    with b2c2_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = b2c2_api.B2c2Api(api_client)

        try:
            # Get Balances
            api_response = api_instance.b2c2_balance_get()
            click.echo(api_response)
        except ApiException as e:
            click.echo("Exception when calling B2c2Api->b2c2_balance_get: %s\n" % e)


@cli.command()
@click.pass_context
def instruments(ctx):
    """List Instruments."""
    configuration = ctx.obj["configuration"]
    with b2c2_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = b2c2_api.B2c2Api(api_client)

        try:
            # Get Instruments
            api_response = api_instance.b2c2_instruments_get()
            click.echo(api_response)
        except ApiException as e:
            click.echo("Exception when calling B2c2Api->b2c2_instruments_get: %s\n" % e)


def validate_side(ctx, param, value):
    if value.lower() not in ("buy", "sell"):
        raise click.BadParameter("""Should be "buy" or "sell".""")
    return value


def validate_quantity(ctx, param, value):
    error = "Should be a positive integer"
    if len(value) > 4:
        raise click.BadParameter("maximum 4 decimals")
    try:
        quantity = int(value)
        if quantity < 1:
            raise click.BadParameter(error)
    except ValueError:
        raise click.BadParameter(error)
    return value


def validate_uuid(ctx, param, value):
    try:
        uuid.UUID(value)
    except ValueError:
        raise click.BadParameter("Should be a UUID")
    return value


def _order(
    configuration,
    instrument,
    side,
    quantity,
    client_order_id,
    price,
    order_type,
    valid_until,
    executing_unit,
):
    with b2c2_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = b2c2_api.B2c2Api(api_client)

        try:
            order_request = OrderRequest(
                instrument=instrument,
                side=side,
                quantity=quantity,
                client_order_id=client_order_id,
                price=price,
                order_type=order_type,
                valid_until=valid_until,
                executing_unit=executing_unit,
            )
            api_response = api_instance.b2c2_order_post(order_request)
            click.echo(api_response)
        except ApiException as e:
            click.echo("Exception when calling B2c2Api->b2c2_order_post: %s\n" % e)


@cli.command("rfq")
@click.argument("instrument")
@click.argument("side", callback=validate_side)
@click.argument("quantity", callback=validate_quantity)
@click.argument("client_rfq_id", callback=validate_uuid)
@click.pass_context
def request_for_quote(ctx, instrument, side, quantity, client_rfq_id):
    """Send Request for Quotes."""
    configuration = ctx.obj["configuration"]
    with b2c2_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = b2c2_api.B2c2Api(api_client)

        try:
            currency = instrument[3:6]  # TODO validate instrument is an accepted input
            balance = api_instance.b2c2_balance_get()
            # currency_balance = float(balance[currency])
            currency_balance = 10000
            click.echo(currency_balance)
            quote_request = QuoteRequest(
                instrument=instrument,
                side=side,
                quantity=quantity,
                client_rfq_id=client_rfq_id,
            )
            quote = api_instance.b2c2_request_for_quote_post(quote_request)
            if currency_balance < (float(quote.price) * float(quote.quantity)):
                click.echo(
                    f"your balance {currency_balance} is not enough to pass this order"
                )
                return
            click.echo("your quote:")
            click.echo(quote)
            click.confirm("do you want to pass this order?", default=None, abort=True)
            client_order_id = str(uuid.uuid4())
            click.echo(f"passing order with order id: {client_order_id}")
            # TODO prompt for order_type
            # TODO prompt for executing_unit
            _order(
                configuration,
                quote.instrument,
                quote.side,
                quote.quantity,
                client_order_id,
                quote.price,
                "FOK",
                quote.valid_until,
                "risk-adding-strategy",
            )
        except ApiException as e:
            click.echo(
                "Exception when calling B2c2Api->b2c2_request_for_quote_post: %s\n" % e
            )


def validate_order_type(ctx, param, value):
    if value.lower() not in ("fok", "mkt"):
        raise click.BadParameter("""Should be "FOK" or "MKT".""")
    return value


@cli.command()
@click.argument("instrument")
@click.argument("side", callback=validate_side)
@click.argument("quantity", callback=validate_quantity)
@click.argument("client_order_id", callback=validate_uuid)
@click.argument("price")  # TODO valicate not negative
@click.argument("order_type", callback=validate_order_type)
@click.argument("valid_until")  # TODO validate date
@click.argument("executing_unit")  # TODO validate
@click.pass_context
def order(
    ctx,
    instrument,
    side,
    quantity,
    client_order_id,
    price,
    order_type,
    valid_until,
    executing_unit,
):
    configuration = ctx.obj["configuration"]
    _order(
        configuration,
        instrument,
        side,
        quantity,
        client_order_id,
        price,
        order_type,
        valid_until,
        executing_unit,
    )
