import warnings

try:
    from importlib.metadata import PackageNotFoundError, version
except ModuleNotFoundError:  # pragma:nocover
    from importlib_metadata import PackageNotFoundError, version

warnings.filterwarnings("ignore", category=Warning, message="distutils Version classes are deprecated")
__appname__ = "grafana_snapshots"

try:
    __version__ = version(__appname__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
