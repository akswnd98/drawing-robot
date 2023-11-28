from bluetooth import *
from motor import *
from path import *

def main():
    global mainloop

    wiringpi.wiringPiSetup()

    try:
        init_all_output_pins()
    except KeyboardInterrupt:
        deinit_all_output_pins()

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()

    adapter = find_adapter(bus)
    if not adapter:
        print('GattManager1 interface not found')
        return

    service_manager = dbus.Interface(
            bus.get_object(BLUEZ_SERVICE_NAME, adapter),
            GATT_MANAGER_IFACE)

    app = Application(bus)

    mainloop = GLib.MainLoop()

    print('Registering GATT application...')

    service_manager.RegisterApplication(app.get_path(), {},
                                    reply_handler=register_app_cb,
                                    error_handler=register_app_error_cb)

    mainloop.run()
    

if __name__ == '__main__':
    main()
