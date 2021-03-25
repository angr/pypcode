PROCESSORS_DIR:=../processors
SPECFILES:=$(shell find $(PROCESSORS_DIR) -name '*.slaspec')
SLAFILES:=$(SPECFILES:.slaspec=.sla)
SLEIGH_BIN:=./bin/sleigh

V = 0
VE_0 := @
VE_1 :=
VE = $(VE_$(V))

ifeq ($(V),1)
QUIET=
else
QUIET=>/dev/null
endif

all: $(SLAFILES)

%.sla: %.slaspec $(SLEIGH_BIN)
	@echo "sleigh  $@"
	$(VE) $(SLEIGH_BIN) $< $@ $(QUIET)

.PHONY: clean
clean:
	$(VE) rm -f $(SLAFILES) $(QUIET)

