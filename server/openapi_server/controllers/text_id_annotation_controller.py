import connexion
import re
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_id_annotation_request import TextIdAnnotationRequest  # noqa: E501
from openapi_server.models.text_id_annotation import TextIdAnnotation
from openapi_server.models.text_id_annotation_response import TextIdAnnotationResponse  # noqa: E501
from openapi_server.neuroner import neuroner

def create_text_id_annotations(text_id_annotation_request=None):  # noqa: E501
    """Annotate IDs in a clinical note

    Return the ID annotations found in a clinical note # noqa: E501

    :param text_id_annotation_request:
    :type text_id_annotation_request: dict | bytes

    :rtype: TextIdAnnotationResponse
    """
    if connexion.request.is_json:
        try:
            annotation_request = TextIdAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
            note = annotation_request._note
            matches = neuroner.annotate(note._text)

            annotations = []
            add_id_annotations(annotations, matches)
            res = TextIdAnnotationResponse(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status, "Missing body")
    return res, status

def add_id_annotations(annotations, matches):
    """
    Converts matches to TextIdAnnotation objects and adds them to the
    annotations array specified.
    """
    # TODO Clarify the source for this list
    id_map = {
        "BIOID":"bio_id",
        "IDNUM": "id_number",
        "MEDICALRECORD" :"medical_record",
        "MEDICAL RECORD" :"medical_record",
        "MEDICAL_RECORD" :"medical_record",
        "SSN": "ssn",
        "DEVICE": "device",
        "ACCOUNT": "account",
        "LICENSE": "license"
    }
    for match in matches:
        if match['type'] in id_map.keys():
            annotations.append(TextIdAnnotation(
                start=match['start'],
                length=len(match['text']),
                text=match['text'],
                id_type=id_map[match['type']],
                confidence=50
            ))
