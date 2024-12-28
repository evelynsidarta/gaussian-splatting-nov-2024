#version 420

layout(location = 0) out vec4 out_color;

in vec3 normal_coord;

void main(void) {
    vec3 color = vec3(normalize(normal_coord));
	   color = color * 0.5 + 0.5;
    out_color = vec4(color, 1.0);
    //out_color = vec4(dot(normal_coord, vec3(0.58,-0.58,0.08)));
    if (length(normal_coord) == 0.0) { // no normal present
        out_color = vec4(0.8);
    }
}