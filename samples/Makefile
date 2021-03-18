#
# Compiles $(TARGET).c for several architectures using dockcross containers
#

ALL_ARCH= \
	linux-mips \
	linux-mipsel \
	linux-arm64 \
	linux-armv5 \
	linux-armv6 \
	linux-armv7 \
	linux-armv7a \
	linux-x64 \
	linux-ppc64le

TARGET=simple_code
ALL_DOCKCROSS=$(addprefix dockcross-, $(ALL_ARCH))
ALL_BINS=$(addprefix $(TARGET)., $(addsuffix .bin, $(ALL_ARCH)))
ALL_OBJS=$(addprefix $(TARGET)., $(addsuffix .o,   $(ALL_ARCH)))

all: $(ALL_BINS)

.PRECIOUS: $(ALL_DOCKCROSS)
dockcross-%:
	@echo "\n\n[**] Getting $@"
	docker pull     $(patsubst dockcross-%, dockcross/%, $@)
	docker run --rm $(patsubst dockcross-%, dockcross/%, $@) > $@
	chmod +x $@

targ_to_arch = $(strip $(patsubst $(TARGET).%, %, $(patsubst %.bin, %, $(1))))
$(TARGET).%.bin: $(TARGET).c dockcross-%
	@echo "\n\n[**] Compiling for $(call targ_to_arch, $@)"
	./dockcross-$(call targ_to_arch, $@) make ARCH=$(call targ_to_arch, $@) target
	mv $@i $@

clean:
	rm -f $(ALL_BINS) $(ALL_OBJS)

# ---

OBJCOPY=$(shell dirname ${CC})/$(CROSS_TRIPLE)-objcopy

target: $(TARGET).$(ARCH).bini

.PRECIOUS: $(TARGET).$(ARCH).o
%.$(ARCH).bini: %.$(ARCH).o
	$(OBJCOPY) -O binary --only-section=.text $< $@

%.$(ARCH).o: %.c
	$(CC) -c -Os -o $@ $<
