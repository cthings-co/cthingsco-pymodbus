#!/usr/bin/env python3
"""Modbus Frame Generator Example.

This example shows how to use ModbusFrameGenerator to create and parse
Modbus frames without actual communication.
"""
from pymodbus.client import ModbusFrameGenerator
from pymodbus.framer import FramerType


def run_frame_generator():
    """Run frame generator example."""
    print("### Modbus Frame Generator Example ###")
    
    # Create generator instance (RTU mode, slave address 1)
    generator = ModbusFrameGenerator(framer=FramerType.RTU, slave=1)

    print("\n1. Generate Request Frames:")
    print("-" * 40)

    # Read Coils Request (FC=1)
    read_coils_frame = generator.read_coils(address=100, count=8)
    print(f"Read Coils (addr=100, count=8):")
    print(f"  Frame: {read_coils_frame.hex()}")

    # Write Single Coil Request (FC=5)
    write_coil_frame = generator.write_coil(address=100, value=True)
    print(f"\nWrite Single Coil (addr=100, value=ON):")
    print(f"  Frame: {write_coil_frame.hex()}")

    # Read Holding Registers Request (FC=3)
    read_regs_frame = generator.read_holding_registers(address=100, count=2)
    print(f"\nRead Holding Registers (addr=100, count=2):")
    print(f"  Frame: {read_regs_frame.hex()}")

    # Write Single Register Request (FC=6)
    write_reg_frame = generator.write_register(address=100, value=1234)
    print(f"\nWrite Single Register (addr=100, value=1234):")
    print(f"  Frame: {write_reg_frame.hex()}")

    print("\n2. Parse Response Frames:")
    print("-" * 40)

    # Parse Read Coils Response (with CRC)
    coils_response = b"\x01\x01\x01\xCD\x81\x88"  # slave 1, FC 1, 1 byte, value 0xCD + CRC
    decoded = generator.parse_response(coils_response)
    print("Read Coils Response:")
    print(f"  Raw: {coils_response.hex()}")
    print(f"  Decoded: {decoded}")

    # Parse Read Holding Registers Response (with CRC)
    regs_response = b"\x01\x03\x04\x00\x0A\x00\x0B\x41\x83"  # slave 1, FC 3, 4 bytes, values [10, 11] + CRC
    decoded = generator.parse_response(regs_response)
    print("\nRead Registers Response:")
    print(f"  Raw: {regs_response.hex()}")
    print(f"  Decoded: {decoded}")


if __name__ == "__main__":
    run_frame_generator() 