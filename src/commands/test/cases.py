from pathlib import Path

from attr import dataclass
from starkware.starknet.testing.objects import StarknetTransactionExecutionInfo
from src.commands.test.test_environment_exceptions import ReportedException


@dataclass
class PassedCase:
    tx_info: StarknetTransactionExecutionInfo


@dataclass
class FailedCase:
    file_path: Path
    function_name: str
    exception: ReportedException


@dataclass
class BrokenTest:
    file_path: Path
    exception: ReportedException
