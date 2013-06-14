//////////////////////////////////////////////////////
//
//       OpenGL Robot Demonstration Program
//  Project work for Computer Graphics Course 20562 
//               by Dennis Sheberla
//
//
//////////////////////////////////////////////////////
#include "TextureLoader.h"
#include "Camera.h"
#include "Robot.h"
#include <GL/glext.h>

#define WINDOW_HEIGHT 600
#define WINDOW_WIDTH 800

#define WINDOW_X_OFFSET 100
#define WINDOW_Y_OFFSET 100


// Camera view modes
#define VIEW_3P 0           // 3rd person
#define VIEW_1P 1           // 1rd person
#define VIEW_LIGHT0 2       // Light 0 positioning
#define VIEW_LIGHT1 3       // Light 1 positioning

//Color edit modes
#define COLOR_EDIT_NONE             0
#define COLOR_EDIT_GLOBAL_AMB       1
#define COLOR_EDIT_LIGHT0_AMB       2
#define COLOR_EDIT_LIGHT0_DIF       3
#define COLOR_EDIT_LIGHT0_SPC       4
#define COLOR_EDIT_LIGHT1_AMB       5
#define COLOR_EDIT_LIGHT1_DIF       6
#define COLOR_EDIT_LIGHT1_SPC       7

#define WINDOW_Y_OFFSET 100

/*-------------- DECLARATIONS ------------------------*/
GLfloat arhead=0;	
GLfloat rheadspeed=0.01;

int mouseX, mouseY;

bool keyStates[256];  // Array of boolean values of length 256 (0-255) for key buffering, true - key is pressed
bool keySpecialStates[256]; //Same for special keys 

//Modes
bool mouseViewMode=false; // true = Mouse Camera Rotation Mode On
bool helpMode=false; // true = Help text display Mode On
int colorEditMode = COLOR_EDIT_NONE; // No color editing by default
int cameraMode = VIEW_3P;  // Set default 3rd person view mode

Robot robot;
Camera camera3P;
Camera cameraL0;
Camera cameraL1;

//Textures
TextureLoader m_TextureLoader;
glTexture m_FloorTexture;
glTexture m_CrateTexture;
glTexture m_BarrelTexture1;
glTexture m_BarrelTexture2;
int floorListNum, barrelListNum;


//Colors
const GLfloat WhiteColor4[]  = { 1.0, 1.0, 1.0, 1.0 };
const GLfloat BlackColor4[]  = { 0.0, 0.0, 0.0, 1.0 };
const GLfloat Gray7Color4[]  = { 0.7, 0.7, 0.7, 1.0 };
const GLfloat Gray5Color4[]  = { 0.5, 0.5, 0.5, 1.0 };
const GLfloat Gray4Color4[]  = { 0.4, 0.4, 0.4, 1.0 };

GLfloat LightGlobalAmbient[] = {0.3,0.3,0.3,1.0};

GLfloat Light0Ambient[]  = { 0.4f, 0.4f, 0.4f, 1.0f };
GLfloat Light0Diffuse[]  = { 1.0f, 1.0f, 1.0f, 1.0f };
GLfloat Light0Specular[] = { 0.8f, 0.8f, 0.8f, 1.0f};
GLfloat Light0Position[] = { 10.0f, 15.0f, 10.0f, 1.0f };

GLfloat Light1Ambient[]  = { 0.0f, 0.0f, 0.0f, 1.0f };
GLfloat Light1Diffuse[]  = { 0.2f, 0.8f, 0.1f, 1.0f };
GLfloat Light1Specular[] = { 0.0f, 0.5f, 0.0f, 1.0f};
GLfloat Light1Position[] = { -10.0f, 15.0f, -10.0f, 1.0f };
GLfloat Light1Direction[] = { 1.0f, -1.0f, 1.0f};

char messageText[1000]="";
char* helpText = "Mouse control:\nLeft click + movement - Control camera/robot viewing direction\nRight click - Main Menu\n\nKeyboard control:\n\nRobot Control\nw - Move forward\ns - Move backward\na - Move left (Strafe left)\nd - Move right (Strafe right)\nq, e - Rotate CW, CCW\nz, x - Rotate head left, right\nc, v - Rotate head up, down\n5, t (g, b) - Rotate right arm (left arm)\n6, y (h, n) - Rotate right forearm (left forearm)\n7, u (j, m) - Rotate right palm (left palm)\n\nCamera control\nArrow Up - Move forward\nArrow Down - Move backward\nArrow Left - Move left (Strafe left)\nArrow Right - Move right (Strafe right)\nPage Up - Move camera upward\nPage Down - Move camera downward\n\nColor edit control\nF2, F3 - increase/decrease bright (all colors)\nF4, F5 - increase/decrease red color\nF6, F7 - increase/decrease green color\nF8, F9 - increase/decrease blue color\nF10 - exit from color editing";
char* helpText1 = "Help\n\nF1 - Show help\nF10 - Exit from help";

/*--------------  Declaration of methods ------------------------*/
void InitGlut(int argc, char **argv);
void SwitchCamera(void);
void InitGl();
void ExitApp(int code);
void SetMaterial(const GLfloat spec[],const GLfloat amb[],const GLfloat diff[], int shin);
void StructFloor (void);
void StructBarrel(void);
void DisplayText(GLint x, GLint y, char* s, GLfloat r, GLfloat g, GLfloat b);
void DrawBarrel(void);
void DrawCrate(void);
void DrawWorld(void);
void ColorControl(GLfloat* color);
void KeyOperations (void);
void Display(void);
void Reshape(GLint newWidth, GLint newHeight);
void keyPressed (unsigned char key, int x, int y);
void keyUp (unsigned char key, int x, int y);
void keySpecialPressed (int key, int x, int y);
void keySpecialUp (int key, int x, int y);
void Mouse(int button, int state, int x, int y);
void MouseMotion(int x, int y);
void Timer(int extra);
void RegisterCallbacks(void);
void MenuSelect(GLint menu);
void GlutMenu(void);
//void main(int argc, char **argv);


/*-------------- IMPLEMENTATION ------------------------*/
//Initialize GLUT
void InitGlut(int argc, char **argv) {
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT);
    glutInitWindowPosition(WINDOW_X_OFFSET, WINDOW_Y_OFFSET);
    glutInit(&argc, argv);
    glutCreateWindow("OpenGL Robot");
    glutWarpPointer(glutGet(GLUT_WINDOW_WIDTH) >> 1,glutGet(GLUT_WINDOW_HEIGHT) >> 1);
    
    m_TextureLoader.SetTextureFilter(txTrilinear);
}


// Initialize GL
void InitGl() {
    
    glClearColor(1.0, 1.0, 1.0, 0.0); //background
    robot.initStructures();  
    glEnable(GL_LIGHTING);
    glShadeModel(GL_SMOOTH);
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LEQUAL);	
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST); // Really Nice Perspective Calculations
    //glEnable(GL_CULL_FACE);
    glEnable(GL_NORMALIZE);
    //glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER,GL_TRUE);
    GLfloat FogCol[3]={0.7f,0.7f,0.7f};
    glEnable(GL_FOG);
    glFogfv(GL_FOG_COLOR,FogCol); // Set the fog color
    glFogi(GL_FOG_MODE,GL_EXP2);  
    glFogf(GL_FOG_DENSITY,0.03f); // Set fog density

    camera3P.set(10,5, -10, 0,0,0, 0,1,0);
    
    if (!m_TextureLoader.LoadTextureFromDisk("parquet1.tga",&m_FloorTexture)) std::cerr<<"Unable to load texture. Disabling."; //Load Texture
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT );
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT );	
    
    if (!m_TextureLoader.LoadTextureFromDisk("crate1.tga",&m_CrateTexture)) std::cerr<<"Unable to load texture. Disabling."; //Load Texture
    if (!m_TextureLoader.LoadTextureFromDisk("barrel1.jpg",&m_BarrelTexture1)) std::cerr<<"Unable to load texture. Disabling."; //Load Texture
    if (!m_TextureLoader.LoadTextureFromDisk("barrel2.jpg",&m_BarrelTexture2)) std::cerr<<"Unable to load texture. Disabling."; //Load Texture
    
    StructFloor();
    StructBarrel();
}


//Init logic
void InitLogic(){
    std::fill_n( keyStates, 256, false); 
    std::fill_n( keySpecialStates, 256, false);
    cameraL0.set(Light0Position[0],Light0Position[1],Light0Position[2],0,0,0,0,1,0);
    cameraL1.set(Light1Position[0],Light1Position[1],Light1Position[2],
        Light1Position[0]+Light1Direction[0],
        Light1Position[1]+Light1Direction[1],
        Light1Position[2]+Light1Direction[2],
        0,1,0);
}

// Define Viewport based on current window size
void DefineViewport(int x, int y, int s) {
    int currH = glutGet(GLUT_WINDOW_HEIGHT);
    int currW = glutGet(GLUT_WINDOW_WIDTH);
    if (currH < currW)
        glViewport(currH * x, currH * y, currH * s, currH * s);
    else
        glViewport(currW * x, currW * y, currW * s, currW * s);
}

//Set Material Properties Specular, ambient, diffusion and shines
void SetMaterial(const GLfloat spec[],const GLfloat amb[],const GLfloat diff[], int shin)
{
    glMaterialfv(GL_FRONT, GL_SPECULAR, spec);
    glMateriali(GL_FRONT, GL_SHININESS, shin);
    glMaterialfv(GL_FRONT, GL_AMBIENT, amb);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diff);
}

//Display Bitmap text
void DisplayText(GLint x, GLint y, char* s, GLfloat r, GLfloat g, GLfloat b)
{
    int lines;
    char* p;
    glPushAttrib(GL_CURRENT_BIT|GL_LIGHTING_BIT);
    glDisable(GL_LIGHTING);
    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity();
    glOrtho(0.0, glutGet(GLUT_WINDOW_WIDTH), 
        0.0, glutGet(GLUT_WINDOW_HEIGHT), -1.0, 1.0);
    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glLoadIdentity();
    glColor3f(r,g,b);
    glRasterPos2i(x, y);
    for(p = s, lines = 0; *p; p++) {
        if (*p == '\n') {
            lines++;
            glRasterPos2i(x, y-(lines*18));
        }
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, *p);
    }
    glPopMatrix();
    glMatrixMode(GL_PROJECTION);
    glPopMatrix();
    glMatrixMode(GL_MODELVIEW);
    glPopAttrib();
}

// Tessellated Floor display list
void StructFloor (void)
{
    int i, j,jj,ii;
    GLfloat x0=-10, z0=-10, x1=1, z1=1;
    int count=15;       // Number of division of the flor block
    int repeat=20;      // Repeat number of floor block

    floorListNum=glGenLists(1);
    glNewList(floorListNum,GL_COMPILE);
    SetMaterial(Gray7Color4,Gray7Color4,Gray4Color4,128);
    if( m_FloorTexture.TextureID )
    {
        glEnable(GL_TEXTURE_2D);
        glBindTexture(GL_TEXTURE_2D, m_FloorTexture.TextureID);			// Select Texture 
    }
    glBegin(GL_QUADS);

    glNormal3f( 0.f,  1.f, 0.f);
    for(jj = 1; jj <= repeat; jj++)
        for(ii = 1; ii <= repeat; ii++) 
            for(j = 0; j < count; j++)
                for(i = 0; i < count; i++)
                {
                    glTexCoord2f(i * 1.f/count, j * 1.f/count);
                    glVertex3f(x0+x1*ii + i * x1 * 1.f/count,
                        0.0,
                        z0+z1*jj + j * z1 * -1.f/count);
                    glTexCoord2f((i + 1) * 1.f/count, j * 1.f/count);
                    glVertex3f(x0+x1*ii + (i + 1) * x1 * 1.f/count,
                        0.0,
                        z0+z1*jj + j * z1 * -1.f/count);
                    glTexCoord2f((i + 1) * 1.f/count, (j + 1) * 1.f/count);
                    glVertex3f(x0+x1*ii + (i + 1) * x1 * 1.f/count,
                        0.0,
                        z0+z1*jj + (j + 1) * z1 * -1.f/count);
                    glTexCoord2f(i * 1.f/count, (j + 1) * 1.f/count);
                    glVertex3f(x0+x1*ii + i * x1 * 1.f/count,
                        0.0,
                        z0+z1*jj + (j + 1) * z1 * -1.f/count);
                }
                glEnd();

        if( m_FloorTexture.TextureID ) glDisable(GL_TEXTURE_2D);
        glEndList();
}

void DrawBarrel(void)										// Draws The Floor
{
    glPushAttrib(GL_TEXTURE_BIT|GL_CURRENT_BIT|GL_ENABLE_BIT|GL_LIGHTING_BIT);
    glCallList(barrelListNum);
    glPopAttrib();
}


// Barrel display list
void StructBarrel(void)
{
    GLUquadricObj *g_cylinder = gluNewQuadric( );
    gluQuadricNormals( g_cylinder, ( GLenum )GLU_SMOOTH );
    gluQuadricTexture( g_cylinder, GL_TRUE );
    GLUquadricObj *g_disk = gluNewQuadric( );
    gluQuadricNormals( g_disk, ( GLenum )GLU_SMOOTH );
    gluQuadricTexture( g_disk, GL_TRUE );

    barrelListNum=glGenLists(1);
    glNewList(barrelListNum,GL_COMPILE);
    
    SetMaterial(WhiteColor4,Gray7Color4,Gray5Color4,128);
    glLightModeli(GL_LIGHT_MODEL_COLOR_CONTROL,GL_SEPARATE_SPECULAR_COLOR);    
    if( m_BarrelTexture2.TextureID )
    {
        glEnable( GL_TEXTURE_2D );
        glTexEnvi( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE );
        glBindTexture( GL_TEXTURE_2D, m_BarrelTexture2.TextureID );
    }
    glPushMatrix();
        glTranslatef(0.0,0.5,0.0);
        glRotatef(-90.0,1,0,0);
        gluDisk(g_disk,0.0,0.2,30,30);
    glPopMatrix();

    glPushMatrix();
        glRotatef(-90.0,1,0,0);
        gluDisk(g_disk,0.0,0.2,30,30);
    glPopMatrix();

    if( m_BarrelTexture1.TextureID )
    {
        glEnable( GL_TEXTURE_2D );
        glTexEnvi( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE );
        glBindTexture( GL_TEXTURE_2D, m_BarrelTexture1.TextureID );
    }
    glPushMatrix();
        glTranslatef(0.0,0.0,0.0);    
        glRotatef(-90.0,1,0,0);
        gluCylinder(g_cylinder,0.2,0.2,.5,30,30);
    glPopMatrix();
    glDisable( GL_TEXTURE_2D );
    glLightModeli(GL_LIGHT_MODEL_COLOR_CONTROL,GL_SINGLE_COLOR);
    glEndList();
}


// Draws the crate
void DrawCrate(void)
{
    glPushAttrib(GL_TEXTURE_BIT|GL_CURRENT_BIT|GL_ENABLE_BIT|GL_LIGHTING_BIT);
    SetMaterial(WhiteColor4,Gray7Color4,Gray7Color4,128);
   
   glScalef(0.25,0.25,0.25);
   if( m_CrateTexture.TextureID )
   {
   glEnable(GL_TEXTURE_2D);
   glBindTexture ( GL_TEXTURE_2D, m_CrateTexture.TextureID);
   }
  glBegin(GL_QUADS);
        // Front Face
        glNormal3f( 0.0f, 0.0f, 1.0f);
        glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f,  1.0f);
        glTexCoord2f(1.0f, 0.0f); glVertex3f( 1.0f, -1.0f,  1.0f);
        glTexCoord2f(1.0f, 1.0f); glVertex3f( 1.0f,  1.0f,  1.0f);
        glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f,  1.0f,  1.0f);
        // Back Face
        glNormal3f( 0.0f, 0.0f,-1.0f);
        glTexCoord2f(1.0f, 0.0f); glVertex3f(-1.0f, -1.0f, -1.0f);
        glTexCoord2f(1.0f, 1.0f); glVertex3f(-1.0f,  1.0f, -1.0f);
        glTexCoord2f(0.0f, 1.0f); glVertex3f( 1.0f,  1.0f, -1.0f);
        glTexCoord2f(0.0f, 0.0f); glVertex3f( 1.0f, -1.0f, -1.0f);
        // Top Face
        glNormal3f( 0.0f, 1.0f, 0.0f);
        glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f,  1.0f, -1.0f);
        glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f,  1.0f,  1.0f);
        glTexCoord2f(1.0f, 0.0f); glVertex3f( 1.0f,  1.0f,  1.0f);
        glTexCoord2f(1.0f, 1.0f); glVertex3f( 1.0f,  1.0f, -1.0f);
        // Bottom Face
        glNormal3f( 0.0f,-1.0f, 0.0f);
        glTexCoord2f(1.0f, 1.0f); glVertex3f(-1.0f, -1.0f, -1.0f);
        glTexCoord2f(0.0f, 1.0f); glVertex3f( 1.0f, -1.0f, -1.0f);
        glTexCoord2f(0.0f, 0.0f); glVertex3f( 1.0f, -1.0f,  1.0f);
        glTexCoord2f(1.0f, 0.0f); glVertex3f(-1.0f, -1.0f,  1.0f);
        // Right face
        glNormal3f( 1.0f, 0.0f, 0.0f);
        glTexCoord2f(1.0f, 0.0f); glVertex3f( 1.0f, -1.0f, -1.0f);
        glTexCoord2f(1.0f, 1.0f); glVertex3f( 1.0f,  1.0f, -1.0f);
        glTexCoord2f(0.0f, 1.0f); glVertex3f( 1.0f,  1.0f,  1.0f);
        glTexCoord2f(0.0f, 0.0f); glVertex3f( 1.0f, -1.0f,  1.0f);
        // Left Face
        glNormal3f(-1.0f, 0.0f, 0.0f);
        glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f, -1.0f);
        glTexCoord2f(1.0f, 0.0f); glVertex3f(-1.0f, -1.0f,  1.0f);
        glTexCoord2f(1.0f, 1.0f); glVertex3f(-1.0f,  1.0f,  1.0f);
        glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f,  1.0f, -1.0f);
    glEnd();
    if( m_CrateTexture.TextureID ) glDisable(GL_TEXTURE_2D);
    glPopAttrib();
}

//Draw Scene
void DrawWorld(void)
{
    glPushMatrix();
        glPushAttrib(GL_TEXTURE_BIT|GL_CURRENT_BIT|GL_ENABLE_BIT|GL_LIGHTING_BIT);
        glLightModeli(GL_LIGHT_MODEL_COLOR_CONTROL,GL_SEPARATE_SPECULAR_COLOR);
        glCallList(floorListNum);
        glLightModeli(GL_LIGHT_MODEL_COLOR_CONTROL,GL_SINGLE_COLOR);
        glPopAttrib();
    glPopMatrix();

    glPushMatrix();
        glTranslatef (-7.0, 0.5, -7.0);
        DrawBarrel();
    glPopMatrix(); 
    glPushMatrix();
        glTranslatef (-7.0, 0.25, -7.0);
        DrawCrate();
    glPopMatrix(); 
    glPushMatrix();
        glTranslatef (7.0, 0.0, -4.0);
        DrawBarrel();
    glPopMatrix();     
    glPushMatrix();
        glTranslatef (7.0, 0.5, -4.5);
        DrawBarrel();
    glPopMatrix();     
    glPushMatrix();
        glTranslatef (7.0, 0.0, -4.5);
        DrawBarrel();
    glPopMatrix();     
    glPushMatrix();
        glTranslatef (7.0, 0.75, 4.5);
        DrawCrate();
    glPopMatrix();    
    glPushMatrix();
        glTranslatef (7.0, 0.25, 4.5);
        DrawCrate();
    glPopMatrix();    
    glPushMatrix();
        glTranslatef (-7.0, 0.25, 4.5);
        DrawCrate();
    glPopMatrix();    
    glPushMatrix();
        glTranslatef (-7.0, 0.75, 4.0);
        DrawCrate();
    glPopMatrix();    
    glPushMatrix();
        glTranslatef (-7.0, 0.25, 4.0);
        DrawCrate();
    glPopMatrix(); 

    //Orientation sphere
    //glPushMatrix();
    //    glRotatef(90.0,1,0,0);
    //    glutWireSphere(30,30,30);
    //glPopMatrix(); 
}

//Switch camera mode
void SwitchCamera(void)
{
    if (cameraMode==VIEW_1P) {
        cameraMode=VIEW_3P;
        glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER,GL_FALSE);
    } else if (cameraMode==VIEW_3P) {
        cameraMode=VIEW_1P;
        glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER,GL_TRUE);
    } else {
        cameraMode=VIEW_3P;
        glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER,GL_FALSE);
    }
}

// Color editing by keyboard
void ColorControl(GLfloat* color)
{
    const GLfloat changeSpeed=0.03f;
    
    // Hi Low
    if (keySpecialStates[GLUT_KEY_F2]) {
        color[0] -= changeSpeed;
        if (color[0] < 0.0) color[0]=0.0;
        if (color[0] > 1.0) color[0]=1.0;

        color[1] -= changeSpeed;
        if (color[1] < 0.0) color[1]=0.0;
        if (color[1] > 1.0) color[1]=1.0;

        color[2] -= changeSpeed;
        if (color[2] < 0.0) color[2]=0.0;
        if (color[2] > 1.0) color[2]=1.0;

    }

    if (keySpecialStates[GLUT_KEY_F3]) {
        color[0] += changeSpeed;
        if (color[0] < 0.0) color[0]=0.0;
        if (color[0] > 1.0) color[0]=1.0;

        color[1] += changeSpeed;
        if (color[1] < 0.0) color[1]=0.0;
        if (color[1] > 1.0) color[1]=1.0;

        color[2] += changeSpeed;
        if (color[2] < 0.0) color[2]=0.0;
        if (color[2] > 1.0) color[2]=1.0;
    }
    
    //Red
    if (keySpecialStates[GLUT_KEY_F4]) {
        color[0] -= changeSpeed;
        if (color[0] < 0.0) color[0]=0.0;
    }
    if (keySpecialStates[GLUT_KEY_F5]) {
        color[0] += changeSpeed;
        if (color[0] > 1.0) color[0]=1.0;
    }

    //Green
    if (keySpecialStates[GLUT_KEY_F6]) {
        color[1] -= changeSpeed;
        if (color[1] < 0.0) color[1]=0.0;
    }
    if (keySpecialStates[GLUT_KEY_F7]) {
        color[1] += changeSpeed;
        if (color[1] > 1.0) color[1]=1.0;
    }

    //Blue
    if (keySpecialStates[GLUT_KEY_F8]) {
        color[2] -= changeSpeed;
        if (color[2] < 0.0) color[2]=0.0;
    }
    if (keySpecialStates[GLUT_KEY_F9]) {
        color[2] += changeSpeed;
        if (color[2] > 1.0) color[2]=1.0;
    }

}

// Process keyboard commands 
void KeyOperations (void) {
    if (keyStates[27]) {
        ExitApp(0);
    }
    if (keyStates['w']) {
        robot.move(robot.moveSpeed);
    }
    if (keyStates['s']) {
        robot.move(-robot.moveSpeed);
    }
    if (keyStates['a']) {
        robot.strafe(robot.moveSpeed);
    }
    if (keyStates['d']) {
        robot.strafe(-robot.moveSpeed);
    }
    if (keyStates['q']) {
        robot.yaw(-robot.moveSpeed);
    }
    if (keyStates['e']) {
        robot.yaw(robot.moveSpeed);
    }
    if (keyStates['5']) {
        robot.moveRightArm(robot.angleSpeed);
    }
    if (keyStates['t']) {
        robot.moveRightArm(-robot.angleSpeed);
    }
    if (keyStates['6']) {
        robot.moveRightForearm(robot.angleSpeed);
    }
    if (keyStates['y']) {
        robot.moveRightForearm(-robot.angleSpeed);
    }
    if (keyStates['7']) {
        robot.moveRightPalm(robot.angleSpeed);
    }
    if (keyStates['u']) {
        robot.moveRightPalm(-robot.angleSpeed);
    }    
    if (keyStates['g']) {
        robot.moveLeftArm(robot.angleSpeed);
    }
    if (keyStates['b']) {
        robot.moveLeftArm(-robot.angleSpeed);
    }
    if (keyStates['h']) {
        robot.moveLeftForearm(robot.angleSpeed);
    }
    if (keyStates['n']) {
        robot.moveLeftForearm(-robot.angleSpeed);
    }
    if (keyStates['j']) {
        robot.moveLeftPalm(robot.angleSpeed);
    }
    if (keyStates['m']) {
        robot.moveLeftPalm(-robot.angleSpeed);
    }
    if (keyStates['z']) {
        robot.moveHeadY(-robot.angleSpeed);
    }
    if (keyStates['x']) {
        robot.moveHeadY(robot.angleSpeed);
    }
    if (keyStates['c']) {
        robot.moveHeadZ(-robot.moveSpeed);
    }
    if (keyStates['v']) {
        robot.moveHeadZ(robot.moveSpeed);
    }
    // Show Help
    if (keySpecialStates[GLUT_KEY_F1]) {
        colorEditMode=COLOR_EDIT_NONE;
        helpMode=true;
    }
    //Exit help mode and color edit mode
    if (keySpecialStates[GLUT_KEY_F10]) {
        colorEditMode=COLOR_EDIT_NONE;
        helpMode=false;
    }

    // Keys for 3 person view mode
    if (cameraMode==VIEW_3P){
        if (keySpecialStates[GLUT_KEY_UP]) {
            camera3P.move(camera3P.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_DOWN]) {
            camera3P.move(-camera3P.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_LEFT]) {
            camera3P.strafe(-camera3P.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_RIGHT]) {
            camera3P.strafe(camera3P.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_PAGE_UP]) {
            camera3P.up(camera3P.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_PAGE_DOWN]) {
            camera3P.up(-camera3P.moveSpeed);
        }
    }
    //Keys for light0 positioning
    if (cameraMode==VIEW_LIGHT0){
        if (keySpecialStates[GLUT_KEY_UP]) {
            cameraL0.move(cameraL0.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_DOWN]) {
            cameraL0.move(-cameraL0.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_LEFT]) {
            cameraL0.strafe(-cameraL0.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_RIGHT]) {
            cameraL0.strafe(cameraL0.moveSpeed);
        }     
        if (keySpecialStates[GLUT_KEY_PAGE_UP]) {
            cameraL0.up(camera3P.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_PAGE_DOWN]) {
            cameraL0.up(-camera3P.moveSpeed);
        }
    }
    //Keys for light1 positioning
    if (cameraMode==VIEW_LIGHT1){
        if (keySpecialStates[GLUT_KEY_UP]) {
            cameraL1.move(cameraL1.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_DOWN]) {
            cameraL1.move(-cameraL1.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_LEFT]) {
            cameraL1.strafe(-cameraL1.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_RIGHT]) {
            cameraL1.strafe(cameraL1.moveSpeed);
        }     
        if (keySpecialStates[GLUT_KEY_PAGE_UP]) {
            cameraL0.up(camera3P.moveSpeed);
        }
        if (keySpecialStates[GLUT_KEY_PAGE_DOWN]) {
            cameraL0.up(-camera3P.moveSpeed);
        }
    }
    Vector3 temp;
    
    // Select light color to edit
    switch (colorEditMode)
    {
    case COLOR_EDIT_GLOBAL_AMB:
        ColorControl(LightGlobalAmbient);
        strcpy(messageText,"Global ambient light color:\n");
        temp.set(LightGlobalAmbient[0],LightGlobalAmbient[1],LightGlobalAmbient[2]);
        strcat(messageText,temp.toString());
        break;
    case COLOR_EDIT_LIGHT0_AMB:
        ColorControl(Light0Ambient);
        strcpy(messageText,"Light0 ambient light color:\n");
        temp.set(Light0Ambient[0],Light0Ambient[1],Light0Ambient[2]);
        strcat(messageText,temp.toString());
        break;
    case COLOR_EDIT_LIGHT0_DIF:
        ColorControl(Light0Diffuse);
        strcpy(messageText,"Light0 diffuse light color:\n");
        temp.set(Light0Diffuse[0],Light0Diffuse[1],Light0Diffuse[2]);
        strcat(messageText,temp.toString());
        break;
    case COLOR_EDIT_LIGHT0_SPC:
        ColorControl(Light0Specular);
        strcpy(messageText,"Light0 specular light color:\n");
        temp.set(Light0Specular[0],Light0Specular[1],Light0Specular[2]);
        strcat(messageText,temp.toString());
        break;
    case COLOR_EDIT_LIGHT1_AMB:
        ColorControl(Light1Ambient);
        strcpy(messageText,"Light1 ambient light color:\n");
        temp.set(Light1Ambient[0],Light1Ambient[1],Light1Ambient[2]);
        strcat(messageText,temp.toString());
        break;
    case COLOR_EDIT_LIGHT1_DIF:
        ColorControl(Light1Diffuse);
        strcpy(messageText,"Light1 diffuse light color:\n");
        temp.set(Light1Diffuse[0],Light1Diffuse[1],Light1Diffuse[2]);
        strcat(messageText,temp.toString());
        break;
    case COLOR_EDIT_LIGHT1_SPC:
        ColorControl(Light1Specular);
        strcpy(messageText,"Light1 specular light color:\n");
        temp.set(Light1Specular[0],Light1Specular[1],Light1Specular[2]);
        strcat(messageText,temp.toString());
        break;
    default:
        strcpy(messageText,"");
        break;
    }
}

// Main display function
void Display(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    KeyOperations();
    
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT,LightGlobalAmbient);
    
    //Vector3 vDir1=cameraL1.getView()-cameraL1.getPosition();
    //DisplayText(0,0,vDir1.toString(),0,0,0);
    DisplayText(0,18,messageText,0.0,0.0,0.0);

    if (helpMode==false) {
    glLoadIdentity(); // Reset The Modelview Matrix

    if (cameraMode==VIEW_1P) robot.setLook(); 
    else if (cameraMode==VIEW_3P) camera3P.setLook();
    else if (cameraMode==VIEW_LIGHT0) {
        Light0Position[0]=cameraL0.getPosition().v[0];
        Light0Position[1]=cameraL0.getPosition().v[1];
        Light0Position[2]=cameraL0.getPosition().v[2];
        cameraL0.setLook();
    } else if (cameraMode==VIEW_LIGHT1) {
        Light1Position[0]=cameraL1.getPosition().v[0];
        Light1Position[1]=cameraL1.getPosition().v[1];
        Light1Position[2]=cameraL1.getPosition().v[2];
        Vector3 vDir=cameraL1.getView()-cameraL1.getPosition();
        Light1Direction[0] = vDir.v[0];
        Light1Direction[1] = vDir.v[1];
        Light1Direction[2] = vDir.v[2];
        cameraL1.setLook();
    }

    glPolygonMode(GL_FRONT,GL_FILL);
    glPolygonMode(GL_BACK,GL_LINE);

    robot.drawRobot();
    glPushMatrix();
        DrawWorld();
    glPopMatrix();
        

    glLightfv(GL_LIGHT0, GL_AMBIENT, Light0Ambient);		// Setup The Ambient Light
    glLightfv(GL_LIGHT0, GL_DIFFUSE, Light0Diffuse);		// Setup The Diffuse Light
    glLightfv(GL_LIGHT0, GL_SPECULAR,Light0Specular);       // Setup The Specular Light
    glLightfv(GL_LIGHT0, GL_POSITION,Light0Position);	// Position The Light
    glEnable(GL_LIGHT0);
   
    glLightfv(GL_LIGHT1, GL_AMBIENT, Light1Ambient);		// Setup The Ambient Light
    glLightfv(GL_LIGHT1, GL_DIFFUSE, Light1Diffuse);		// Setup The Diffuse Light
    glLightfv(GL_LIGHT1, GL_SPECULAR,Light1Specular);       // Setup The Specular Light
    glLightfv(GL_LIGHT1, GL_POSITION,Light1Position);	// Position The Light
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION,Light1Direction);	// Direction The Light
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF,10.0);
    glLighti(GL_LIGHT1, GL_SPOT_EXPONENT,64);
    glEnable(GL_LIGHT1);   

     } else {
         DisplayText(0,glutGet(GLUT_WINDOW_HEIGHT)-18, helpText,0.0, 0.5, 0.0);
         DisplayText(400,glutGet(GLUT_WINDOW_HEIGHT)-90, helpText1,0.0, 0.5, 0.5);
    }
    glutSwapBuffers();
}


//Resize display
void Reshape(GLint newWidth, GLint newHeight)
{
    glViewport(0,0, (GLsizei)newWidth, (GLsizei)newHeight);

    glMatrixMode(GL_PROJECTION);     // Select The Projection Matrix
    glLoadIdentity();                // Reset The Projection Matrix
    // Calculate The Aspect Ratio And Set The Clipping Volume
    if (newHeight == 0) newHeight = 1; // Zero-division prevention
    gluPerspective(30.0f, (GLfloat)newWidth/(GLfloat)newHeight, 0.1, 100.0);

    glMatrixMode(GL_MODELVIEW);      // Select The Modelview Matrix
}

//Exit App release textures
void ExitApp(int code)
{
    m_TextureLoader.FreeTexture(&m_FloorTexture);
    m_TextureLoader.FreeTexture(&m_CrateTexture);
    m_TextureLoader.FreeTexture(&m_BarrelTexture1);
    m_TextureLoader.FreeTexture(&m_BarrelTexture2);
    exit(code);
}

// Update keyboard buffer
void keyPressed (unsigned char key, int x, int y) {
    keyStates[key] = true; // Set the state of the current key to pressed
    //glutPostRedisplay();
}

// Update keyboard buffer
void keyUp (unsigned char key, int x, int y) {
    keyStates[key] = false; // Set the state of the current key to not pressed
}

// Update keyboard buffer
void keySpecialPressed (int key, int x, int y) {
    if ((key>=0)&&(key<=255))
        keySpecialStates[key] = true; // Set the state of the current key to pressed
    //glutPostRedisplay();
}

// Update keyboard buffer
void keySpecialUp (int key, int x, int y) {
    if ((key>=0)&&(key<=255))
        keySpecialStates[key] = false; // Set the state of the current key to not pressed
}


// Process mouse buttons
void Mouse(int button, int state, int x, int y) {

    if (button == GLUT_LEFT_BUTTON) {
        if (state == GLUT_DOWN) 
        {
            int middleX = glutGet(GLUT_WINDOW_WIDTH) >> 1; 
            int middleY = glutGet(GLUT_WINDOW_HEIGHT) >> 1;
            glutWarpPointer(middleX,middleY);
            glutSetCursor(GLUT_CURSOR_NONE);
            mouseViewMode=true;
        } 
        else if (state == GLUT_UP)
        {
            glutSetCursor(GLUT_CURSOR_RIGHT_ARROW);
            mouseViewMode=false;
        }
    }

}

// Process mouse motion
void MouseMotion(int x, int y) {
    if (mouseViewMode==true){
        if (cameraMode==VIEW_3P){
            camera3P.setViewByMouse(x,y,300,100);
            //glutPostRedisplay();
        } else if (cameraMode==VIEW_1P)
        {
            robot.setViewByMouse(x,y,1000,1000);
            //glutPostRedisplay();
        } else if (cameraMode==VIEW_LIGHT0) {
            cameraL0.setViewByMouse(x,y,300,100);
            //glutPostRedisplay();
        } else if (cameraMode==VIEW_LIGHT1) {
            cameraL1.setViewByMouse(x,y,300,100);
            //glutPostRedisplay();
        }
    }
}


// Sets timer for refresh the display
void Timer(int extra)
{
    glutPostRedisplay();
    glutTimerFunc(30,Timer,0);
}


// Register glut Callbacks
void RegisterCallbacks(void) {
    glutDisplayFunc(Display);
    glutReshapeFunc(Reshape);
    glutSpecialFunc(keySpecialPressed);
    glutSpecialUpFunc(keySpecialUp);
    glutKeyboardFunc(keyPressed);
    glutKeyboardUpFunc(keyUp);
    glutMouseFunc(Mouse);
    glutMotionFunc(MouseMotion);
    //glutIdleFunc(Keyboard);
    glutTimerFunc(0,Timer,0);
}


// Process the menu
void MenuSelect(GLint menu) 
{
    switch (menu) {
    case 9999:
        ExitApp(0);
        break;
    case 1:
        SwitchCamera();
        break;
    case 2:
        colorEditMode=COLOR_EDIT_GLOBAL_AMB;
        break;
    case 31:
        cameraMode=VIEW_LIGHT0;
        break;
    case 32:
        colorEditMode=COLOR_EDIT_LIGHT0_AMB;
        break;
    case 33:
        colorEditMode=COLOR_EDIT_LIGHT0_DIF;
        break;
    case 34:
        colorEditMode=COLOR_EDIT_LIGHT0_SPC;
        break;
    case 41:
        cameraMode=VIEW_LIGHT1;
        break;
    case 42:
        colorEditMode=COLOR_EDIT_LIGHT1_AMB;
        break;
    case 43:
        colorEditMode=COLOR_EDIT_LIGHT1_DIF;
        break;
    case 44:
        colorEditMode=COLOR_EDIT_LIGHT1_SPC;
        break;
    case 1000:
        helpMode=!helpMode;
        break;
    }
    glutPostRedisplay();
}

// Create the menu
void GlutMenu(void)
{
    int light0Menu,light1Menu;
    light0Menu=glutCreateMenu(MenuSelect);
    glutAddMenuEntry("Set position (camera view)",31);
    glutAddMenuEntry("Change ambient color",32);
    glutAddMenuEntry("Change diffuse color",33);
    glutAddMenuEntry("Change specular color",34);

    light1Menu=glutCreateMenu(MenuSelect);
    glutAddMenuEntry("Set position (camera view)",41);
    glutAddMenuEntry("Change ambient color",42);
    glutAddMenuEntry("Change diffuse color",43);
    glutAddMenuEntry("Change specular color",44);

    glutCreateMenu(MenuSelect);
    glutAddMenuEntry("Switch View (1P <--> 3P)",1);
    glutAddMenuEntry("Adjust Ambient Light",2);
    glutAddSubMenu("Light 0",light0Menu);
    glutAddSubMenu("Light 1 (Spot)",light1Menu);
    glutAddMenuEntry("Help",1000);
    glutAddMenuEntry("Exit",9999);
    glutAttachMenu(GLUT_RIGHT_BUTTON);
}


// Program entering point
int main(int argc, char **argv) {
    InitLogic();
    InitGlut(argc, argv);
    InitGl();
    RegisterCallbacks();
    GlutMenu();
    glutMainLoop();
    ExitApp(0);
    return 0;
}
