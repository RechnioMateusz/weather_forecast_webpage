"""Tests for device application."""
from datetime import datetime

from django.test import TestCase

from device.serializers import UnixTimestampField


class UnixTimeStampFieldTestCase(TestCase):
    def test_can_convert_int_values(self):
        f = UnixTimestampField()
        dt = f.to_internal_value(1584222107)
        self.assertEqual(dt.year, 2020)
        self.assertEqual(dt.month, 3)
        self.assertEqual(dt.day, 14)
        self.assertEqual(dt.hour, 21)
        self.assertEqual(dt.minute, 41)
        self.assertEqual(dt.second, 47)
        self.assertEqual(dt.microsecond, 0)

    def test_can_convert_float_values(self):
        f = UnixTimestampField()
        dt = f.to_internal_value(1584222107.123)
        self.assertEqual(dt.year, 2020)
        self.assertEqual(dt.month, 3)
        self.assertEqual(dt.day, 14)
        self.assertEqual(dt.hour, 21)
        self.assertEqual(dt.minute, 41)
        self.assertEqual(dt.second, 47)
        self.assertEqual(dt.microsecond, 123000)

    def test_can_convert_dt_with_microseconds(self):
        f = UnixTimestampField()
        dt = datetime(2020, 3, 14, 21, 41, 47, 123000)
        ts = f.to_representation(dt)
        self.assertAlmostEqual(ts, 1584222107.123)