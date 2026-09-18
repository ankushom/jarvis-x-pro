import psutil
import socket


def get_system_info():

    try:
        battery = psutil.sensors_battery()

        battery_percent = battery.percent if battery else 0

    except:
        battery_percent = 0

    try:

        socket.create_connection(
            ("8.8.8.8",53),
            timeout=2
        )

        internet = True

    except:

        internet = False

    return {

        "cpu": psutil.cpu_percent(),

        "ram": psutil.virtual_memory().percent,

        "battery": battery_percent,

        "internet": internet

    }