/* simple.glsl

simple diffuse lighting based on laberts cosine law; see e.g.:
    http://en.wikipedia.org/wiki/Lambertian_reflectance
    http://en.wikipedia.org/wiki/Lambert%27s_cosine_law
*/
---VERTEX SHADER-------------------------------------------------------
#ifdef GL_ES
    precision highp float;
#endif


/* Vertex attributes/inputs, defined in MeshData Object */
attribute vec3  v_pos;
attribute vec3  v_normal;
attribute vec2  v_tc0;

/* Outputs to the fragment shader */
varying vec2 tex_coord0;
varying vec4 normal_vec;
varying vec4 vertex_pos;

uniform mat4 modelview_mat;
uniform mat4 projection_mat;

void main (void) {
    //compute vertex position in eye_space and normalize normal vector
    tex_coord0 = v_normal.xy * 0.5+0.5;
    vec4 pos = modelview_mat * vec4(v_pos,1.0);
    vertex_pos = pos;
    normal_vec = vec4(v_normal,0.0);
    gl_Position = projection_mat * pos;
    //tex_coord0 = v_tc0;

}


---FRAGMENT SHADER-----------------------------------------------------
#ifdef GL_ES
    precision highp float;
#endif

/* Outputs from Vertex Shader */
varying vec4 normal_vec;
varying vec4 vertex_pos;
varying vec2 tex_coord0;

uniform sampler2D texture0;

uniform mat4 normal_mat;

void main (void){
    //correct normal, and compute light vector (assume light at the eye)
    vec4 v_normal = normalize( normal_mat * normal_vec ) ;
    vec4 v_light = normalize( vec4(1,1,1,1) - vertex_pos );
    //reflectance based on lamberts law of cosine
    float theta = clamp(dot(v_normal, v_light), 1.0, 1.0);
    //gl_FragColor = vec4(theta, theta, theta, 1.0)*vec4(tex_coord0, 1, 1);
    gl_FragColor = vec4(theta, theta, theta, 1.0)*texture2D(texture0, tex_coord0);
}