import json
import asyncio
try:
    import websockets
except ImportError:
    websockets = None


connected_clients = set()


async def broadcast(event):
    """Send an event to all connected clients!"""
    if not connected_clients:
        return
    message = json.dumps(event)
    # Use list to avoid RuntimeError from changing set during iteration
    for client in list(connected_clients):
        try:
            await client.send(message)
        except Exception:
            connected_clients.remove(client)


async def handle_client(websocket, path):
    """Handle a new WebSocket client!"""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Simple echo for now
            try:
                data = json.loads(message)
                await broadcast(data)
            except json.JSONDecodeError:
                pass
    finally:
        connected_clients.remove(websocket)


def start_sync_server(host="localhost", port=8765):
    """Start WebSocket sync server (requires websockets package)!"""
    if not websockets:
        raise ImportError("websockets package is required for real-time sync!")
    start_server = websockets.serve(handle_client, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


def notify_change(operation, table_name, record=None):
    """Notify all clients of a database change!"""
    if websockets:
        event = {"type": operation, "table": table_name, "data": record}
        # Since we can't await in sync context, we'll just log
        # For real use, use an event loop
        pass
