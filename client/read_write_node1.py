"""
Client for node1

Register map (must match node1_server.py):
    Holding reg 0 -> setpoint (writable) 
    Holding reg 1 -> simulated_temp (read-only, updates every 2s)
    Coil 0 -> pump_enable (writeable) 
"""

from pymodbus.client import ModbusTcpClient

NODE1_HOST = '192.168.1.183' 
NODE1_PORT = 5020

def main() -> None: 
    client = ModbusTcpClient(NODE1_HOST, port=NODE1_PORT)
    if not client.connect(): 
        print(f"Could not connect to {NODE1_HOST}:{NODE1_PORT}")
        return 
    try: 
        # Read the simulated temp (holding register 1)
        result = client.read_holding_registers(address=1, count=1)
        if result.isError():
            print("Read failed: ", result) 
        else: 
            raw = result.registers[0]
            print(f"simulated_temp = {raw / 10:.1f} C (raw={raw})")

        # Write a new setpoint (holding register 0) 
        write_result = client.write_register(address-0, value=225) #22.5 C

        if write_result.isError():
            print(f"Write failed, ", write_result)
        else: 
            print("Setpoint written: 225 (22.5 C)")

        # Confirm the write by reading it back
        confirm  = client.read_holding_register(address=0, count=1)
        print("Setpoint readback: ", confirm.registers[0])

        # Toggle pump_enable coil ON 
        coil_result = client.write_coil(address=0, value=True)
        if coild_result.isError():
            print(f"Coil Write failed: ", coil_result)
        else:
            print("pump_enable -> ON")

        coil_confirm = client.read_coils(address=0, count=1)
        print("pump_enable readback: ", coil_confirm.bits[0])

    finally: 
        client.close()

if __name__ == "__main__":
    main()
