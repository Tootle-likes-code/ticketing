from typing import Optional

from address import Address


class Residence:
    address: Address
    rent_per_month: int
    land_lord: Optional[object]
    rental_payments: list[object] = []
    tenant: Optional[object] = None

    @property
    def is_rented(self):
        return self.tenant is not None
