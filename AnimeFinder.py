import imgui

imgui.create_context()
imgui.get_io().display_size = 800, 600
imgui.get_io().fonts.get_tex_data_as_rgba32()

imgui.new_frame()

imgui.begin("Anime Finder", True)

imgui.text("sono un testo")

imgui.end()

imgui.render()
imgui.end_frame()