import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='line', parent_name='violin.box', **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Line',
            data_docs="""
            color
                Sets the inner box plot bounding line color.
            width
                Sets the inner box plot bounding line width.
""",
            **kwargs
        )
