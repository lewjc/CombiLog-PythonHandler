from enum import Enum


class ClosureCodes(Enum):
    UNREGISTERED_SERVICE = 4000
    INVALID_CONNECTION_QUERY_PARAM = 4001
    INVALID_SECRET = 4002
    SECRET_IN_USE = 4003


error_mappings = {
    ClosureCodes.UNREGISTERED_SERVICE.value: "No service was found for the supplied secret.",
    ClosureCodes.INVALID_CONNECTION_QUERY_PARAM.value: "Missing query parameter 'connectionType' in connection url.",
    ClosureCodes.INVALID_SECRET.value: "Secret supplied was not in the required format: String.",
    ClosureCodes.SECRET_IN_USE.value: "Secret supplied is already in use by another service.",
}


def get_closure_error(closure_code):
    if closure_code in error_mappings.keys():
        return error_mappings[closure_code]
    else:
        return "Unknown Closure Code. Please check aggregator logs."
