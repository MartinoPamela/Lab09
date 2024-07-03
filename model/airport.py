from dataclasses import dataclass


@dataclass
class Airport:
    _ID: int
    _IATA_CODE: str
    _AIRPORT: str
    _CITY: str
    _STATE: str
    _COUNTRY: str
    _LATITUDE: float
    _LONGITUDE: float
    _TIMEZONE_OFFSET: float

    @property
    def ID(self):
        return self._ID

    @property
    def IATA_CODE(self):
        return self._IATA_CODE

    @property
    def AIRPORT(self):
        return self._AIRPORT

    @property
    def CITY(self):
        return self._CITY

    @property
    def STATE(self):
        return self._STATE

    @property
    def COUNTRY(self):
        return self._COUNTRY

    @property
    def LATITUDE(self):
        return self._LATITUDE

    @property
    def LONGITUDE(self):
        return self._LONGITUDE

    @property
    def TIMEZONE_OFFSET(self):
        return self._TIMEZONE_OFFSET

    def __hash__(self):
        return self._ID

    def __str__(self):
        return self.AIRPORT

    def __repr__(self):
        return self.AIRPORT
