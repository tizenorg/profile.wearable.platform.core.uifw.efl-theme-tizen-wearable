prefix ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)/$(prefix)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
SRC=efl-theme-tizen-wearable-circle

all:
	edje_cc $(EDJE_FLAGS) $(EDJE_FLAGS_$(V)) \
		-id ./HVGA/images/\
		-id ./HVGA/images/Bottom_button\
		-id ./HVGA/images/Button\
		-id ./HVGA/images/Controller\
		-id ./HVGA/images/End_effect\
		-id ./HVGA/images/End_effect/Bottom\
		-id ./HVGA/images/End_effect/Left\
		-id ./HVGA/images/End_effect/Right\
		-id ./HVGA/images/End_effect/Top\
		-id ./HVGA/images/Indicator\
		-id ./HVGA/images/Indicator/Horizontal_dot\
		-id ./HVGA/images/List\
		-id ./HVGA/images/List/progress\
		-id ./HVGA/images/No_items\
		-id ./HVGA/images/Option\ popup\
		-id ./HVGA/images/Popup\
		-id ./HVGA/images/Progress\
		-id ./HVGA/images/Progress/Processing_full\
		-id ./HVGA/images/Progress/Processing_popup\
		-id ./HVGA/images/Progress/Processing_small\
		-id ./HVGA/images/Progress/Progress_full\
		-id ./HVGA/images/Progress/Progress_popup\
		-id ./HVGA/images/Progress/Progress_small\
		-id ./HVGA/images/Scroll\
		-id ./HVGA/images/Thumbnail\
		-id ./HVGA/images/Time_picker\
		-id ./HVGA/images/Title_bar\
		-id ./HVGA/images/No_items\
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
