from src.protostar_exception import ProtostarException


class InstallationException(ProtostarException):
    pass


class InvalidLocalRepository(InstallationException):
    pass
