prefix ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)/$(prefix)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
SRC=tizen
SIZE=216x432

all:
	for s in $(SIZE); do \
		cp $(SRC).edc $(SRC)-$(TARGET).edc; \
		perl -pi -e "s/TIZEN_TMP_INC/\"default-inc.edc\"/g" $(SRC)-$(TARGET).edc; \
		edje_cc $(EDJE_FLAGS_$(V))\
		-id ./$$s/images/\
		-id ./$$s/images/Controls\
		-id ./$$s/images/Controls\/number_picker\
		-id ./$$s/images/Navigation_elements\
		-id ./$$s/images/Popups\
		-id ./$$s/images/activity_indicator_sequence\
		-id ./$$s/images/tiny_activity_indicator_sequence\
		$(SRC)-$(TARGET).edc $(SRC)-$(TARGET).edj; \
	done

clean:
	for s in $(SIZE); do \
		rm -rf $(SRC)-$(TARGET).*; \
	done

install:
	mkdir -p $(THEME_DIR)
	for s in $(SIZE); do \
		$(INSTALL) $(SRC)-$(TARGET).edj $(THEME_DIR); \
	done

uninstall:
	rm -rf $(THEME_DIR)/

distclean: clean
