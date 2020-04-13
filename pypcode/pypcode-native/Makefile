LIBSLA=sleigh-2.1.0/src/libsla.a

pypcode-native.so: $(LIBSLA) pypcode-native.cc pypcode-native.h
	gcc -shared -o $@ \
		-Wl,--whole-archive $(LIBSLA) -Wl,--no-whole-archive \
		-fPIC pypcode-native.cc

$(LIBSLA):
	make -C sleigh-2.1.0/src CFLAGS="-fPIC" libsla.a
