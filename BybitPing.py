import asyncio
import json
import time
import websockets


ws_url = "wss://stream.bybit.com/v5/public/linear"


async def send_ping():
    ping_msg = json.dumps({"req_id": "0141585", "op": "ping"})
    async with websockets.connect(ws_url) as ws:
        while True:
            await asyncio.sleep(1)
            t1 = time.perf_counter_ns()
            await ws.send(ping_msg)
            await ws.recv()
            t2 = time.perf_counter_ns()
            rtt = (t2-t1) / 1000000
            print(f'[PING]: {rtt}ms')


if __name__ == '__main__':
    asyncio.run(send_ping())
