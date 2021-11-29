from dataclasses import dataclass

from ukpostcodeutils import validation


@dataclass
class Address:
    house_number: int
    house_name: str
    city: str
    county: str
    post_code: str

    def __post_init__(self):
        if not self._validate_post_code():
            raise ValueError("Postcode was invalid.")

    def _validate_post_code(self):
        return validation.is_valid_postcode(self.post_code)
