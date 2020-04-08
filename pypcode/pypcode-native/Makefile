LIBSLA=sleigh-2.1.0/src/libsla.a

pypcode-native.so: $(LIBSLA)
	gcc -shared -o $@ -Wl,--whole-archive $(LIBSLA) -Wl,--no-whole-archive

$(LIBSLA):
	make -C sleigh-2.1.0/src CFLAGS="-fPIC" libsla.a
