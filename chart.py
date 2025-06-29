import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


def create_chart(categories, values, chart_type, title=None, xlabel=None, ylabel=None, color=None):
    """
    Creates a matplotlib figure based on inputs and returns it.

    Args:
        categories (list of str): Category labels.
        values (list of float): Numeric values.
        chart_type (str): 'bar', 'pie', or 'line'.

    Returns:
        matplotlib.figure.Figure: The created chart figure.
    """

    fig, ax = plt.subplots()

    if chart_type == "bar":
        ax.bar(categories, values, color= color or 'skyblue')
        ax.set_xlabel(xlabel or 'Categories')
        ax.set_ylabel(ylabel or 'Values')
        ax.set_title(title or 'Bar Chart')
    elif chart_type == 'pie':
        ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.set_title('Pie Chart')
        ax.axis('equal')
    elif chart_type == 'line':
        ax.plot(categories, values, marker='o', linestyle='-', color= color or 'green')
        ax.set_xlabel(xlabel or 'Categories')
        ax.set_ylabel(ylabel or 'Values')
        ax.set_title(title or 'Line Chart')
    else:
        raise ValueError("Unsupported chart type. Choose 'bar', 'pie', or 'line'.")

    fig.tight_layout()
    return fig
