"""
Sentient-SONIC Logging Utilities

Structured logging for training, evaluation, and deployment pipelines.
"""

import logging
import os
import sys
from datetime import datetime
from typing import Optional


def setup_logger(
    name: str = "sentient",
    level: int = logging.INFO,
    log_dir: Optional[str] = None,
    console: bool = True,
) -> logging.Logger:
    """
    Configure a structured logger for Sentient-SONIC.

    Args:
        name: Logger name.
        level: Logging level.
        log_dir: Directory for log files. None for console-only.
        console: Whether to also log to console.

    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if console:
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fh = logging.FileHandler(os.path.join(log_dir, f"sentient_{timestamp}.log"))
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


class MetricsLogger:
    """Log training and evaluation metrics to TensorBoard and CSV."""

    def __init__(self, log_dir: str, experiment_name: str = "sentient_sonic"):
        self.log_dir = log_dir
        self.experiment_name = experiment_name
        self._step = 0
        self._writer = None

    def log_scalar(self, tag: str, value: float, step: Optional[int] = None) -> None:
        step = step or self._step
        # Mocked: In production, writes to TensorBoard
        pass

    def log_dict(self, metrics: dict, step: Optional[int] = None) -> None:
        for k, v in metrics.items():
            self.log_scalar(k, v, step)

    def increment_step(self) -> None:
        self._step += 1

    def close(self) -> None:
        if self._writer:
            self._writer.close()
