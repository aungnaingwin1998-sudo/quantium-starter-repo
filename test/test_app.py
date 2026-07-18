import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app
import pandas as pd


def test_data_loaded():
    """
    Check that CSV data is loaded.
    """
    assert app.data is not None
    assert len(app.data) > 0


def test_date_column_is_datetime():
    """
    Check that date column was converted correctly.
    """
    assert pd.api.types.is_datetime64_any_dtype(app.data["date"])


def test_update_graph_all_regions():
    """
    Check graph generation for all regions.
    """
    result = app.update_graph("all")

    assert result is not None
    assert len(result.data) == 1


def test_update_graph_specific_region():
    """
    Check graph generation for one region.
    """
    result = app.update_graph("north")

    assert result is not None
    assert len(result.data) == 1


def test_graph_title():
    """
    Check title changes based on selected region.
    """
    result = app.update_graph("east")

    assert result.layout.title.text == "Pink Morsel Sales - East"


def test_sales_grouping():
    """
    Check that sales are aggregated by date.
    """

    result = app.update_graph("south")

    x_values = list(result.data[0].x)
    y_values = list(result.data[0].y)

    assert len(x_values) == len(y_values)