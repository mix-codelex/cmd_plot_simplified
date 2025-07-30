import os
import sys
import click
from cmd_plot.utils import parse_numbers, sort_points_by_x
from cmd_plot.plots import plot_scatter, plot_line, plot_bar, plot_pie
from importlib.metadata import version as importlib_version


@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Show cmd_plot version")
def cli(version):
    """
    Cli for plotting terminal based graphs
    """
    if version:
        pkg_version = importlib_version("cmd_plot")
        click.echo(f"cmd_plot:{pkg_version}")


@click.command()
@click.option("--data", required=True, help="Comma-separated data")
@click.option("--labels", required=True, help="Comma-separated labels")
@click.option("--width", default=30, help="Width of the bar plot")
def bar(data, labels, width):
    """Create a bar plot

    Args:
        data (_type_): bar data
        labels (_type_): bar labels
        width (_type_): width of the bar plot
    """

    data = [float(x) for x in data.split(",")]
    labels = labels.split(",")
    plot_bar(data, labels, width)


@click.command()
@click.option("--x", required=True, help="Comma-separated x-axis data")
@click.option("--y", required=True, help="Comma-separated y-axis data")
@click.option("--height", default=20, help="Height of the scatter plot")
@click.option("--width", default=50, help="Width of the scatter plot")
def scatter(x, y, height, width):
    """Create a scatter plot"""

    data_x = parse_numbers(x)
    data_y = parse_numbers(y)
    # Sort points for visual correctness especially for line plots
    data_x, data_y = sort_points_by_x(data_x, data_y)
    plot_scatter(data_x, data_y, height=height, width=width)


@click.command()
@click.option("--x", required=True, help="Comma-separated x-axis data")
@click.option("--y", required=True, help="Comma-separated y-axis data")
@click.option("--height", default=20, help="Height of the line plot")
@click.option("--width", default=50, help="Width of the line plot")
def line(x, y, height, width):
    """Create a line plot"""

    data_x = parse_numbers(x)
    data_y = parse_numbers(y)
    data_x, data_y = sort_points_by_x(data_x, data_y)
    plot_line(data_x, data_y, height=height, width=width)


@click.command()
@click.option("--data", required=True, help="Comma-separated data")
@click.option("--labels", required=True, help="Comma-separated labels")
@click.option("--size", default=30, help="size of the pie chart")
def pie(data, labels, size):
    """Create a pie chart"""
    data = parse_numbers(data)
    labels = labels.split(",")
    plot_pie(data, labels, size)


# Add subcommands
cli.add_command(bar)
cli.add_command(scatter)
cli.add_command(line)
cli.add_command(pie)

if __name__ == "__main__":
    cli()
