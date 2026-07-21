"""
Node Server 1 - Simulated Modbus TCP Device 

Register Map for this node (wire addresses, 0-based): 
    Holding registers (FC 03 read / FC 06, 16 write): 
        0 -> Setpoint       (writable, starts at 0) 
        1 -> simulated_temp (read-only) 
    Coil (FC 01 read / FC 05, 15 write):
        0 -> pump_enable    (writeable, starts OFF) 
"""

import asyncio 
import logging

from pymodbus.datastore import(
        ModbusSlaveContext,
        ModbusServerContext,
        ModbusSequentialDataBlock,
)
from pymodbus.server import StartAsyncTcpServer

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("node1")

HOST = "0.0.0.0"
PORT = 5020

'''
Each block is pre-sized; values default to 0
1-Based starting address internally (subtract 1) 
'''
def build_context() -> ModbusServerContext: 
    holding_regs = ModbusSequentialDataBlock(1, [0]*10)
    coils = ModbusSequentialDataBlock(1, [0] * 10)
    discrete_inputs = ModbusSequentialDataBlock(1, [0] * 10)
    input_regs = ModbusSequentialDataBlock(1, [0] * 10)

    slave = ModbusSlaveContext(
            di = discrete_inputs,
            co = coils,
            ir = input_regs,
            hr = holding_regs,
    )

    return ModbusServerContext(slaves=slave, single=True)

async def simulate_temperature(context: ModbusServerContext) -> None: 
    '''
    Background Task: Nudge holding register 1 up/down 1 to mimic a live device sensor changing
    '''

    value = 200
    direction = 1 
    while True:
        await asyncio.sleep(2)
        value += direction * 2 
        if value > 260 or value < 180:
            direction *= -1
        context[0].async_setValues(3,1,[value])
        # device_id = 0, func_cdoe = 3, address = 1, value = new temp
        log.info("node1: simulated_temp register -> %s (%.1f C)", value, value / 10)

async def main() -> None: 
    context = build_context() # build the object holding the devices
    log.info("node1 starting on %s:%s", HOST, PORT)
    asyncio.create_task(simulate_temperature(context))
    await StartAsyncTcpServer(context=context, address=(HOST, PORT))

if __name__ == "__main__":
    asyncio.run(main())

    
