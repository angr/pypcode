SLEIGH_DIR:=sleigh
PROCESSORS_DIR:=processors
SPECFILES:=$(shell find $(PROCESSORS_DIR) -name '*.slaspec')
SLAFILES:=$(SPECFILES:.slaspec=.sla)
SLEIGH_BIN:=$(SLEIGH_DIR)/sleigh_opt
LIBSLA:=$(SLEIGH_DIR)/libsla.a
PYPCODE_NATIVE:=pypcode-native.so

V = 0
VE_0 := @
VE_1 :=
VE = $(VE_$(V))

ifeq ($(V),1)
QUIET=
else
QUIET=>/dev/null
endif

all: $(PYPCODE_NATIVE) $(SLAFILES)

$(PYPCODE_NATIVE): $(LIBSLA) pypcode-native.cc pypcode-native.h
	@echo "cc      $@"
	$(VE) gcc -shared -o $@ \
		-Wl,--whole-archive $(LIBSLA) -Wl,--no-whole-archive \
		-fPIC pypcode-native.cc

%.sla: %.slaspec $(SLEIGH_BIN)
	@echo "sleigh  $@"
	$(VE) $(SLEIGH_BIN) $< $@ $(QUIET)

$(LIBSLA):
	@echo "make    $@"
	$(VE) $(MAKE) -C $(SLEIGH_DIR) CFLAGS="-fPIC" libsla.a $(QUIET)

$(SLEIGH_BIN):
	@echo "make    $@"
	$(VE) $(MAKE) -C $(SLEIGH_DIR) sleigh_opt $(QUIET)

.PHONY: clean
clean:
	$(VE) $(MAKE) -C $(SLEIGH_DIR) reallyclean $(QUIET)
	$(VE) rm -f $(PYPCODE_NATIVE) $(SLAFILES) $(QUIET)
