#version 420

uniform vec3 color;

out vec4 out_color;

void main(void) {
    out_color = vec4(color, 1.0);
}
