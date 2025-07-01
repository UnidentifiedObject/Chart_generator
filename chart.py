import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


def create_chart(categories, datasets, chart_type, title=None, xlabel=None, ylabel=None):
    fig, ax = plt.subplots()

    if chart_type == "bar":
        width = 0.8 / len(datasets)
        x = range(len(categories))
        for i, dataset in enumerate(datasets):
            offset = [xi + i * width for xi in x]
            ax.bar(offset, dataset["values"], width=width, label=dataset["label"], color=dataset.get("color", None))
        ax.set_xticks([xi + width * (len(datasets) - 1) / 2 for xi in x])
        ax.set_xticklabels(categories)

    elif chart_type == "line":
        for dataset in datasets:
            ax.plot(categories, dataset["values"], marker='o', linestyle='-', label=dataset["label"], color=dataset.get("color", None))

    elif chart_type == "pie":
        # Only use first dataset
        dataset = datasets[0]
        ax.pie(dataset["values"], labels=categories, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

    else:
        raise ValueError("Unsupported chart type. Choose 'bar', 'pie', or 'line'.")

    ax.set_title(title or f"{chart_type.capitalize()} Chart")
    ax.set_xlabel(xlabel or 'Categories')
    ax.set_ylabel(ylabel or 'Values')
    if chart_type != "pie":
        ax.legend()

    fig.tight_layout()
    return fig
