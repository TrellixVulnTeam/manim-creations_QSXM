from manim import *
from numuse import  converters
import numuse.music
from fractions import Fraction
import math


SCALE = 12

def create_line_graph(x_values, y_values, x_start, x_end, width, height ):
    plane = NumberPlane(
        #x_range = (math.floor(min(x_values)), math.ceil(max(x_values))),
        x_range = (x_start, x_end),
        y_range = (min(y_values)-1, max(y_values)+1),
        #x_length = self.camera.frame_width - 2 * x_padding,
        x_length = width,
        #y_length = self.camera.frame_height - 2 * y_padding,
        y_length = height,
        #axis_config={"include_numbers": True},
        axis_config={"include_numbers": False},
    )
    plane.center()
    line_graph = plane.get_line_graph(
        x_values = x_values,
        y_values = y_values,
        line_color=GOLD_E,
        vertex_dot_style=dict(stroke_width=10,  fill_color=PURPLE),
        stroke_width = 5,
    )
    labels = VGroup()


    offset_scale = 0.5
    for i in range(len(x_values)):
        x_pos = x_values[i]
        y_pos = y_values[i]
        # assuming plot of more than 2 notes
        assert len(x_values) >= 2
        if i == 0:
            #about to figure out the direction of it 
            y_next = y_values[i+1]
            if y_next > y_pos:
                # put text 
                annotate_offset = [0, offset_scale]
            else:
                annotate_offset = [0, -offset_scale]
        elif i == len(x_values)-1:
            y_prev = y_values[i-1]
            if y_prev > y_pos:
                # put text 
                annotate_offset = [0, offset_scale]
            else:
                annotate_offset = [0, -offset_scale]
        else:
            y_prev = y_values[i-1]
            y_next = y_values[i+1]
            between = y_prev <= y_pos <= y_next or y_prev >= y_pos >= y_next
            if between:
                # downhill
                if y_prev >= y_pos:
                    annotate_offset = [0, offset_scale]
                else:
                    annotate_offset = [0, -offset_scale]
            elif y_pos <= y_prev:
                # v formation put text in v
                annotate_offset = [0, offset_scale]
            elif y_pos >= y_prev:
                # mountain top put text under peak
                annotate_offset = [0, -offset_scale]

        # add z componenent
        annotate_offset.append(0)
        label = Tex(str(y_values[i] % 12), color=BLACK).scale(.5)
        print(annotate_offset)
        #labels.add(label.next_to(line_graph["vertex_dots"][i], np.array(annotate_offset)))
        labels.add(label.move_to(line_graph["vertex_dots"][i]))


    return VGroup(plane, line_graph, labels)



class LineGraphExample(Scene):
    def construct(self):


        self.camera.background_color = WHITE
        
        width=SCALE* 1
        height=SCALE * math.sqrt(2)


        b = 1
        # half
        h = 1 / 2
        # thirds
        t = Fraction(b, 3)
        # two thirds
        tt = 2 * t

        jens_solo_arps = [
            [("0' 4' 7' 11' R", [tt, t, tt, t + b, b])],
            [("R 7' 4' 7' 7'", [tt, t, tt, t + b, b])],
            [("9' 6' R", [b + tt, t + b, b])],
            [("6' 2' 9' 6' 0'' 9' R", [tt, t, tt, t, tt, t, b])],
            [("5' 2' 9' 0'' 5'", [tt, t, tt, t + b, b])],
            [("2' 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
            [("4' 4' 4' 0'", [b, tt, t + b, b])],
            [("11 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
            [("4' 0' R 4' R 4' R 4'", [tt, t, tt, t, tt, t, tt, t])],
            [("7' 4' 7' 7' R 11'", [tt, t, tt, t, 1 + tt, t])],
            [("0'' 0'' 9' R 9' 6'", [b, tt, t, tt, t, b])],
            [("R 2' 2' 2' R", [b, b, tt, t, b])],
            [("0'' 0'' 9' R 9' 5'", [b, tt, t, tt, t, b])],
            [("R 2' 11 5' 2' 11 7", [b, tt, t, tt, t, tt, t])],
            [("4' 0' R 4' 0' R", [tt, t, tt, t, b, b])],
            [("7' 4' 7' 10' R", [tt, t, tt, t + b, b])],
            [("R 9 0' 9 0' 9", [b, b, tt, t, tt, t])],
            [("5 9 0' 4' R", [tt, t, tt, t + b, b])],
            [("R 0' 4' 0' R", [b, b, tt, t, b])],
            [("9 0' 5 R", [b, tt, t + b, b])],
            [("2' R 0'' 6' 9' 6'", [b, b, tt, t, tt, t])],
            [("0'' 0'' 9' R", [b, tt, t + b, b])],
            [("9' R 9' 2' 5' 2'", [b, b, tt, t, tt, t])],
            [("11 11 2' R", [b, tt, t + b, b])],
            [("4' 0' 7' 0' R 4' 7' 11'", [tt, t, tt, t, tt, t, tt, t + b])],
            [("7' 11' R", [tt, t + b, b])],
            [("6' 2' 9' 2' R 9'", [tt, t, tt, t, b, b])],
            [("0'' 6' R 9' R", [tt, t, tt, t + b, b])],
            [("9' 2' R 5' 2'", [tt, t, tt, t + b, b])],
            [("5' 11 R 2' 5'", [tt, t, tt, t + b, b])],
            [("4' 0' 7' 4' 7' 11'", [tt, t, tt, t, tt, t + b])],
            [("R", [4 * b])],
        ]

        all_graphs = VGroup()
        points = []
        measures = converters.parse_music_measures(jens_solo_arps)
        num_lines = len(measures) // 4
        graph_height = height / num_lines
        m = numuse.music.Music(measures, 120)

        def convert_points_to_x_y_list(points):
            return zip(*points)

        point_row = []
        measure_count = 0
        for measure in m.measures:
            # TODO remove hardcoded 4
            if measure_count % 4 == 0 and measure_count != 0:
                x_vals, y_vals = convert_points_to_x_y_list(point_row)
                points.append((x_vals, y_vals))
                point_row = []

            for line in measure.lines:
                for moment in line.moments:
                    if len(moment.notes.notes) != 0:
                       point_row.append((moment.time, list(moment.notes.notes)[0].note))
            measure_count += 1
        #print([float(x) for x in x_vals], [float(y) for y in y_vals])

        # adds in the last one
        points.append(tuple(convert_points_to_x_y_list(point_row)))


        # If the input was less than one measure
        if measure_count <= 4:
            points.append(tuple(convert_points_to_x_y_list(point_row)))

        graphs = []
        start_idx = 0
        for point_row in points:
            row_length = 4 * 4
            x_vals, y_vals = point_row
            graphs.append(create_line_graph(x_vals, y_vals, start_idx, start_idx + row_length, width, graph_height))
            start_idx += row_length

        all_graphs = VGroup(*graphs)
        #all_graphs.arrange(DOWN, buff=0.5)
        all_graphs.arrange(DOWN,buff=0)
        #print(all_graphs.height)
        #config.frame_height = all_graphs.height 
        #config.frame_size = (1080, all_graphs.height * Pixels)
        self.add(all_graphs)

