prefix ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)/$(prefix)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
SRC=efl-theme-tizen-wearable

all:
	edje_cc $(EDJE_FLAGS) $(EDJE_FLAGS_$(V)) \
		-id ./HVGA/images/\
		-id ./HVGA/images/Action_bar\
		-id ./HVGA/images/Action_bar/Activity\
		-id ./HVGA/images/Body\
		-id ./HVGA/images/Button\
		-id ./HVGA/images/Controller_icon\
		-id ./HVGA/images/List\
		-id ./HVGA/images/Overscrolling\
		-id ./HVGA/images/Overscrolling/Bottom\
		-id ./HVGA/images/Overscrolling/Left\
		-id ./HVGA/images/Overscrolling/Right\
		-id ./HVGA/images/Overscrolling/Top\
		-id ./HVGA/images/Option\ popup\
		-id ./HVGA/images/Popup\
		-id ./HVGA/images/Progress\
		-id ./HVGA/images/Progress/Activity\
		-id ./HVGA/images/Scroll\
		-id ./HVGA/images/Slider\
		-id ./HVGA/images/TimePicker\
		-id ./HVGA/images/Title_bar\
		-id ./HVGA/images/Search\
		-id ./HVGA/images/Focus\
		-id ./HVGA/images/temp\
		-id ./HVGA/images/temp/Copy_Paste\
		-id ./HVGA/images/Emoticon\
		-id ./HVGA/images/temp/swipe\
		-id ./HVGA/images/Map\
		-sd ./HVGA/sounds -fd ../objects \
		$(SRC).edc $(SRC).edj; \

clean:
	rm -rf $(SRC).edj;

install:
	mkdir -p $(THEME_DIR)
	$(INSTALL) $(SRC).edj $(THEME_DIR);

uninstall:
	rm -rf $(THEME_DIR)/

distclean: clean
