#version 420

#define VERTICAL_FLIP (0)

layout(location = 0) in vec2 in_vertex;
layout(location = 1) in vec2 in_texcoord;


out vec2 tex_coord;

void main(void) {
	gl_Position = vec4(in_vertex, 0.0, 1.0);
	tex_coord.x = in_texcoord.x;
	if (VERTICAL_FLIP==1) {
		tex_coord.y = 1.0 - in_texcoord.y;
	}
	else {
		tex_coord.y = in_texcoord.y;
	}
}