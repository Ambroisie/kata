#! /usr/bin/env python
import click

from calculator.eval import Evaluator
from calculator.parse import parse_infix, parse_postfix, parse_prefix
from calculator.print import Printer

STR_TO_PARSER = {
    "infix": parse_infix,
    "prefix": parse_prefix,
    "postfix": parse_postfix,
}


@click.group(invoke_without_command=True, chain=True)
@click.option(
    "--expr-type",
    default="infix",
    type=click.Choice(["infix", "prefix", "postfix"], case_sensitive=False),
)
@click.pass_context
def cli(ctx, expr_type):
    ctx.ensure_object(dict)
    ctx.obj["input"] = STR_TO_PARSER[expr_type](
        input(f"Input your {expr_type} expression: ")
    )
    if ctx.invoked_subcommand is None:
        ctx.invoke(eval_tree)


@cli.command(name="print")
@click.pass_context
def print_tree(ctx):
    """
    Print the parsed AST.
    """
    Printer().print(ctx.obj["input"])


@cli.command(name="eval")
@click.pass_context
def eval_tree(ctx):
    """
    Evaluate the parsed expression.
    """
    print(Evaluator().visit_and_get_value(ctx.obj["input"]))


if __name__ == "__main__":
    cli(obj={})
