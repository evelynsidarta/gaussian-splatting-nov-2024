#version 420

uniform vec3 lightDir;

out vec4 out_color;

in vec3 color_vert;
in vec3 vertexPos; 
in vec3 normalPos;

void main(void) {
	float kd = 0.2;
	vec3 normal = normalize(normalPos);
	vec3 shading = max(0.0,dot(lightDir,normal))*color_vert;
	
	out_color = vec4( (1.0-kd)*color_vert + kd*shading, 1.0);
	//out_color = vec4( normal , 1.0 );
}
