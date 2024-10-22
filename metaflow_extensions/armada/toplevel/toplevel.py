"""Toplevel imports will be available on metaflow module level"""

__mf_extensions__ = "armada-metaflow"

from ..plugins import armada
from ..plugins.armada_decorator import ArmadaDecorator
from ..plugins import armada_cli


__mf_promote_submodules__ = []

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("armada-metaflow").version
except Exception:
    # this happens on remote environments since the job package
    # does not have a version
    __version__ = None
