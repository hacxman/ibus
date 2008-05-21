import weakref
import gobject
import ibus

class Engine (ibus.Object):
	__gsignals__ = {
		"commit-string" : (
			gobject.SIGNAL_RUN_FIRST,
			gobject.TYPE_NONE,
			(gobject.TYPE_STRING, )),
		"forward-key-event" : (
			gobject.SIGNAL_RUN_FIRST,
			gobject.TYPE_NONE,
			(gobject.TYPE_UINT, gobject.TYPE_UINT, gobject.TYPE_UINT )),
		"preedit-changed" : (
			gobject.SIGNAL_RUN_FIRST,
			gobject.TYPE_NONE,
			(gobject.TYPE_STRING, gobject.TYPE_PYOBJECT, gobject.TYPE_UINT)),
		"aux-string-changed" : (
			gobject.SIGNAL_RUN_FIRST,
			gobject.TYPE_NONE,
			(gobject.TYPE_STRING, gobject.TYPE_PYOBJECT)),
		"update-lookup-table" : (
			gobject.SIGNAL_RUN_FIRST,
			gobject.TYPE_NONE,
			(gobject.TYPE_PYOBJECT, )),
		"show-lookup-table" : (
			gobject.SIGNAL_RUN_FIRST,
			gobject.TYPE_NONE,
			()),
		"hide-lookup-table" : (
			gobject.SIGNAL_RUN_FIRST,
			gobject.TYPE_NONE,
			())
	}

	def __init__ (self, ibusconn, object_path):
		ibus.Object.__init__ (self)
		self._ibusconn = ibusconn
		self._object_path = object_path
		self._engine = ibusconn.get_object (self._object_path)
		self._lookup_table = ibus.LookupTable ()
		self._ibusconn.connect ("destroy", self._ibusconn_destroy_cb)

	def handle_dbus_signal (self, message):
		if message.is_signal (ibus.IBUS_ENGINE_IFACE, "CommitString"):
			args = message.get_args_list ()
			self.emit ("commit-string", args[0])
			return True
		elif message.is_signal (ibus.IBUS_ENGINE_IFACE, "ForwardKeyEvent"):
			args = message.get_args_list ()
			self.emit ("forward-key-event", args[0], arg[1], arg[2])
			return True
		elif message.is_signal (ibus.IBUS_ENGINE_IFACE, "PreeditChanged"):
			args = message.get_args_list ()
			attrs = ibus.attr_list_from_dbus_value (args[1])
			self.emit ("preedit-changed", args[0], attrs, args[2])
			return True
		elif message.is_signal (ibus.IBUS_ENGINE_IFACE, "AuxStringChanged"):
			args = message.get_args_list ()
			attrs = ibus.attr_list_from_dbus_value (args[1])
			self.emit ("aux-string-changed", args[0], attrs)
			return True
		elif message.is_signal (ibus.IBUS_ENGINE_IFACE, "UpdateLookupTable"):
			args = message.get_args_list ()
			lookup_table = ibus.lookup_table_from_dbus_value (args[0])
			self.emit ("update-lookup-table", lookup_table)
			return True
		elif message.is_signal (ibus.IBUS_ENGINE_IFACE, "ShowLookupTable"):
			args = message.get_args_list ()
			self.emit ("show-lookup-table")
			return True
		elif message.is_signal (ibus.IBUS_ENGINE_IFACE, "HideLookupTable"):
			args = message.get_args_list ()
			self.emit ("hide-lookup-table")
			return True
		else:
			return False

	def focus_in (self):
		self._engine.FocusIn (**ibus.DEFAULT_ASYNC_HANDLERS)

	def focus_out (self):
		self._engine.FocusOut (**ibus.DEFAULT_ASYNC_HANDLERS)

	def reset (self):
		self._engine.Reset (**ibus.DEFAULT_ASYNC_HANDLERS)

	def process_key_event (self, keyval, is_press, state, reply_cb, error_cb):
		self._engine.ProcessKeyEvent (keyval, is_press, state, 
									reply_handler = reply_cb,
									error_handler = error_cb)
	
	def set_cursor_location (self, x, y, w, h):
		self._engine.SetCursorLocation (x, y, w, h)

	def set_enable (self, enable):
		self._engine.SetEnable (enable)

	def destroy (self):
		ibus.Object.destroy (self)
		if self._engine:
			self._engine.Destroy ()
			self._engine = None
		self._ibusconn = None

	def _ibusconn_destroy_cb (self, ibusconn):
		self._engine = None
		self.destroy ()

gobject.type_register (Engine)

