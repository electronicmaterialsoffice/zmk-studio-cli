from rich.console import Console
from rich.style import Style

error_style = Style(color="red1", bold=True)
notification_style = Style(color="dark_slate_gray3", bold=True)
console = Console()


def log_dbg(subsystem: str, *args, **kwargs):
    """Print to console"""
    console.print(f"<dbg, {subsystem}>", *args, **kwargs)


def log_err(subsystem: str, *args, **kwargs):
    """Print to console with error style"""
    console.print(f"[red1]<err, {subsystem}>", *args, **kwargs, style=error_style)


def log_notif(subsystem: str, *args, **kwargs):
    """Print to console with notification style"""
    console.print(
        f"[dark_slate_gray3]<notif, {subsystem}>",
        *args,
        **kwargs,
        style=notification_style,
    )
