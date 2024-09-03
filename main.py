from src.smart_tv_converter import SmartTVConverter

if __name__ == "__main__":
    tv_model = "Generic 40-inch LED TV"
    screen_size = 40
    converter = SmartTVConverter(tv_model, screen_size)
    converter.detect_tv()
    converter.install_apps()
    converter.add_free_channels()
    converter.add_free_streaming_apps()
    converter.update_system()
    converter.save_configuration("config/smart_tv_config.json")

    total_size = converter.calculate_total_size()
    print(f"Total size of the Smart TV Converter software: {total_size:.2f} GB")

    converter.app.run(host='0.0.0.0', port=5000)
