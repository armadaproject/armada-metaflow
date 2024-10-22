###
# CONFIGURE: Define additional plugins here. Your defined plugins will typically fall
#            into one of the categories defined below
###

STEP_DECORATORS_DESC = [("armada", ".armada_decorator.ArmadaDecorator")]

###
# Force a certain set of decorators
###
# EXAMPLE: This example sets a given set of decorators and will ignore all toggles and
# user settings
ENABLED_STEP_DECORATOR = ["batch", "airflow_internal", "armada"]

CLIS_DESC = [("armada", ".armada_cli.cli")]

###
# CONFIGURE: Similar to datatools, you can make visible under metaflow.plugins.* other
#            submodules not referenced in this file
###
__mf_promote_submodules__ = []
