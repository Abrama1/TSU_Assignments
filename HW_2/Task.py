from abc import ABC, abstractmethod


class BaseRecord(ABC):
    """
    Abstract base class for a single EV data record.

    Fields:
        region, parameter, powertrain, year, unit, value
    """

    def __init__(self, region, parameter, powertrain, year, unit, value):
        """
        Initialize a common EV record.

        Args:
            region (str): Geographic region.
            parameter (str): Metric type.
            powertrain (str): EV type (BEV(Battery Electric Vehicle), PHEV(Plugin Hybrid EV), EV).
            year (int): Year of the data.
            unit (str): Unit of measurement.
            value (float): Recorded value.
        """
        self.region = region
        self.parameter = parameter
        self.powertrain = powertrain
        self.year = year
        self.unit = unit
        self.value = value

    @abstractmethod
    def describe(self):
        """
        Return a short human readable description of record.

        Must be implemented in subclasses.
        """
        pass

    def to_dict(self):
        """
        Convert this record into a dictionary.

        Returns:
            dict: Dictionary with all record fields.
        """
        return {
            "region": self.region,
            "parameter": self.parameter,
            "powertrain": self.powertrain,
            "year": self.year,
            "unit": self.unit,
            "value": self.value,
        }

    def __repr__(self):
        """
        Return a debug representation of the record.

        Returns:
            str: String showing the main fields.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.region!r}, {self.parameter!r}, {self.powertrain!r}, "
            f"{self.year!r}, {self.unit!r}, {self.value!r})"
        )

    def __eq__(self, other):
        """
        Compare records based on all fields.

        Returns:
            bool: True if all the fields are equal.
        """
        if not isinstance(other, BaseRecord):
            return False
        return (
            self.region == other.region
            and self.parameter == other.parameter
            and self.powertrain == other.powertrain
            and self.year == other.year
            and self.unit == other.unit
            and self.value == other.value
        )

    def __hash__(self):
        """
        Make the record hashable, so we can put it into a set.

        Returns:
            int: Hash of all important fields.
        """
        return hash(
            (
                self.region,
                self.parameter,
                self.powertrain,
                self.year,
                self.unit,
                self.value,
            )
        )


class EVRecord(BaseRecord):
    """
    Concrete record for electric vehicle statistics.

    Inherits common fields from BaseRecord.
    """

    def describe(self):
        """
        Build a readable description for this EV record.

        Returns:
            str: Description containing region, year, parameter and value.
        """
        return (
            f"In {self.year} in {self.region}, '{self.parameter}' "
            f"for {self.powertrain} was {self.value} {self.unit}."
        )

    def is_percentage(self):
        """
        Check if the unit of this record is a percentage.

        Returns:
            bool: True if the unit represents a percent value.
        """
        unit_lower = self.unit.lower()
        return unit_lower == "percent" or unit_lower == "%" or unit_lower == "percentage"

    @staticmethod
    def analyze_sales_by_region_year(records, region, unit, start_year, end_year):
        """
        Sum values for a given region, unit and year range.

        Args:
            records (iterable): Collection of EVRecord objects.
            region (str): Region to filter by.
            unit (str): Unit to filter by.
            start_year (int): Start of year interval (inclusive).
            end_year (int): End of year interval (inclusive).

        Returns:
            float: Sum of values for all matching records.
        """
        total = 0.0
        for rec in records:
            if (
                rec.region == region
                and rec.unit == unit
                and start_year <= rec.year <= end_year
            ):
                total += rec.value
        return total

    @staticmethod
    def count_entries_with_value_less_than(records, parameter, powertrain, unit, max_value):
        """
        Count records that match given fields and have value < max_value.

        Args:
            records (iterable): Collection of EVRecord objects.
            parameter (str): Parameter to filter by.
            powertrain (str): EV type.
            unit (str): Unit of measurement.
            max_value (float): Upper bound for value.

        Returns:
            int: Number of records satisfying all conditions.
        """
        count = 0
        for rec in records:
            if (
                rec.parameter == parameter
                and rec.powertrain == powertrain
                and rec.unit == unit
                and rec.value < max_value
            ):
                count += 1
        return count
