from typing import Dict

from graph_builder.graph.operator import Operator
from graph_builder.graph.operators.attributes.first_inplace import FirstInplace
from graph_builder.graph.operators.attributes.post_axiswise import PostAxiswise
from graph_builder.graph.operators.attributes.post_elementwise import PostElementwise
from graph_builder.graph.variable import Variable


class ElementwiseSum(Operator):
    """
    n入力を加算するレイヤー
    """
    attributes = {PostElementwise,
                  PostAxiswise,
                  FirstInplace}

    def __init__(self, name: str, parameters: Dict[str, object] = None):
        """
        :param name: 
        :param parameters: 
        """
        super().__init__(name, parameters)

    def __call__(self, *xs: Variable):
        y = Variable(xs[0].shape, xs[0].axis_order)
        for i, x in enumerate(xs):
            self.append_input(f"x{i}", x)
        self.append_output("y", y)
        return y,