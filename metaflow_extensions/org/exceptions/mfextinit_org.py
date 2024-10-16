"""armada-metaflow specific exceptions"""

from metaflow.exception import MetaflowException


class ArmadaException(MetaflowException):
    """Generic armada-metaflow Exception"""

    headline = "Armada error"

    def __init__(self):
        super().__init__("The armada-metaflow extension encountered a problem.")
