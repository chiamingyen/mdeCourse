#include "Robot.h"
#include <iostream>
#include <GL/glut.h>
#include <GL/glext.h>

// Radians to Degrees conversion
#ifndef _180_OVER_PI
#define  _180_OVER_PI   57.29577951308232087665461840231273527024 
#endif

#define BODY			1 
#define HEAD			2
#define ARM		        3
#define PALM		    5
#define FOREARM	        7

using namespace std;

// Robot related Constants
const float Robot::HEAD_Y_POS=1.1;
const float Robot::HEAD_Y_ANGLE_MAX=1.3;
const float Robot::HEAD_Z_ANGLE_MAX=0.5;
const float Robot::HEAD_Z_MAX=0.5;
const float Robot::PALM_ANGLE_MAX=40.0;
const float Robot::FOREARM_ANGLE_MAX=110.0;

// Material colors
static GLfloat mat_specularGRAY[]  ={0.75,0.75,0.75,1.0};
static GLfloat mat_ambientGRAY[]   ={0.5,0.5,0.5,1.0};
static GLfloat mat_diffuseGRAY[]   ={0.50,0.50,0.50,1.0};
static GLfloat mat_shininessGRAY[] ={128.0 * 0.6};

static GLfloat mat_specularGRAY1[]  ={0.5,0.5,0.5,1.0};
static GLfloat mat_ambientGRAY1[]   ={0.4,0.4,0.4,1.0};
static GLfloat mat_diffuseGRAY1[]   ={0.4,0.4,0.5,1.0};
static GLfloat mat_shininessGRAY1[] ={128.0 * 0.3};

static GLfloat mat_specularBLUE[]  ={0.75,0.75,0.75,1.0};
static GLfloat mat_ambientBLUE[]   ={0,0,1,1.0};
static GLfloat mat_diffuseBLUE[]   ={0.50,0.50,0.50,1.0};
static GLfloat mat_shininessBLUE[] ={128.0 };

static GLfloat mat_specularYELLOW[] ={0.75,0.75,0.75,1.0};
static GLfloat mat_ambientYELLOW[] ={1,1,0,1.0};
static GLfloat mat_diffuseYELLOW[] ={0.50,0.50,0.50,1.0};
static GLfloat mat_shininessYELLOW[] ={128.0};

static GLfloat mat_specularRED[] ={0.75,0.75,0.75,1.0};
static GLfloat mat_ambientRED[] ={1.0,0.0,0.0,1.0};
static GLfloat mat_diffuseRED[] ={0.50,0.50,0.50,1.0};
static GLfloat mat_shininessRED[] ={128.0};

Robot::Robot(void)
{
    moveSpeed  = 0.05;
    angleSpeed = 3.0;

    headAngleY       =0.0;
    headAngleZ       =0.0;
    rightArmAngle    =0.0;
    leftArmAngle     =0.0;
    rightForearmAngle=0.0;
    leftForearmAngle =0.0;
    rightPalmAngle   =10.0;
    leftPalmAngle    =10.0;

    m_pPosition  = Vector3(0.0, 0.0, 0.0);        // Position Point
    m_vHeadView  = Vector3(1.0, 0.0, 0.0);      // Head view Vector
    m_vDirection = Vector3(1.0, 0.0, 0.0);        // Robot direction Vector
    
    _TextureLoader.SetTextureFilter(txTrilinear); //Mipmaping

}


Robot::~Robot(void)
{
    _TextureLoader.FreeTexture(&m_BodyTexture);
}

void Robot::set( float positionX, float positionY, float positionZ,   
                  float viewX,     float viewY,     float viewZ)   
{   
    //  
    Vector3 Position    = Vector3(positionX, positionY, positionZ);   
    Vector3 HeadView        = Vector3(viewX, viewY, viewZ);   
    
   
    //
    m_pPosition = Position;     
    m_vHeadView = HeadView;             
    
}

// Arm Movement controls
void Robot::moveRightArm(float speed){
    rightArmAngle = (GLfloat)((int)(rightArmAngle + speed) % 360);
}

void Robot::moveLeftArm(float speed){
    leftArmAngle = (GLfloat)((int)(leftArmAngle + speed) % 360);
}

void Robot::moveRightForearm(float speed){
    if (rightForearmAngle>FOREARM_ANGLE_MAX) rightForearmAngle=FOREARM_ANGLE_MAX;
    if (rightForearmAngle<-FOREARM_ANGLE_MAX) rightForearmAngle=-FOREARM_ANGLE_MAX;
    rightForearmAngle = rightForearmAngle + speed;
}

void Robot::moveRightPalm(float speed){
    if (rightPalmAngle>PALM_ANGLE_MAX) rightPalmAngle=PALM_ANGLE_MAX;
    if (rightPalmAngle<-PALM_ANGLE_MAX) rightPalmAngle=-PALM_ANGLE_MAX;
    rightPalmAngle = rightPalmAngle + speed;
}

void Robot::moveLeftForearm(float speed){
    if (leftForearmAngle>FOREARM_ANGLE_MAX) leftForearmAngle=FOREARM_ANGLE_MAX;
    if (leftForearmAngle<-FOREARM_ANGLE_MAX) leftForearmAngle=-FOREARM_ANGLE_MAX;
    leftForearmAngle = leftForearmAngle + speed;
}

void Robot::moveLeftPalm(float speed){
    if (leftPalmAngle>PALM_ANGLE_MAX) leftPalmAngle=PALM_ANGLE_MAX;
    if (leftPalmAngle<-PALM_ANGLE_MAX) leftPalmAngle=-PALM_ANGLE_MAX;
    leftPalmAngle = leftPalmAngle + speed;
}

void Robot::moveHeadY(float speed){
    if (headAngleY > HEAD_Y_ANGLE_MAX*_180_OVER_PI) headAngleY=HEAD_Y_ANGLE_MAX*_180_OVER_PI; // Restrict movement around Y axis
    if (headAngleY < -HEAD_Y_ANGLE_MAX*_180_OVER_PI) headAngleY=-HEAD_Y_ANGLE_MAX*_180_OVER_PI; // Restrict movement around Y axis
    headAngleY = headAngleY + speed; //Update rotation angle for display

    m_vHeadView.v[0] = (float)(cos(headAngleY/_180_OVER_PI)*m_vDirection.v[0] - sin(headAngleY/_180_OVER_PI)*m_vDirection.v[2]);   
    m_vHeadView.v[2] = (float)(sin(headAngleY/_180_OVER_PI)*m_vDirection.v[0] + cos(headAngleY/_180_OVER_PI)*m_vDirection.v[2]); 
    m_vHeadView.normalize();
}

void Robot::moveHeadZ(float speed){

    m_vHeadView.v[1] += speed;
    if ((m_vHeadView.v[1] < -HEAD_Z_MAX)) m_vHeadView.v[1] = -HEAD_Z_MAX;   // Restrict movement around Z axis
    if ((m_vHeadView.v[1] > HEAD_Z_MAX)) m_vHeadView.v[1] = HEAD_Z_MAX;     // Restrict movement around Z axis
        
    headAngleZ = asinf(m_vHeadView.v[1]/m_vHeadView.length())* _180_OVER_PI; //Update rotation angle for display
}

void Robot::setLook(void)
{

    Vector3 pPosCorr=m_pPosition + m_vHeadView*0.2;     // Correct view point to the head size
    
    // Set camera view
    gluLookAt(pPosCorr.v[0], HEAD_Y_POS, pPosCorr.v[2],    
        pPosCorr.v[0]+m_vHeadView.v[0], HEAD_Y_POS+m_vHeadView.v[1], pPosCorr.v[2]+m_vHeadView.v[2],       
        0.0, 1.0, 0.0); 
}

// Move forward/backward
void Robot::move(float speed)
{
       
    m_pPosition.v[0] += m_vDirection.v[0] * speed;       
    m_pPosition.v[2] += m_vDirection.v[2] * speed;      
        
}

// Move left/right
void Robot::strafe(float speed)
{
    Vector3 vOrtho;              // Orthogonal vector for the view vector    

    vOrtho.v[0] = -m_vDirection.v[2];   
    vOrtho.v[2] =  m_vDirection.v[0];   

    //   update position
    m_pPosition.v[0]  +=  vOrtho.v[0] * speed;   
    m_pPosition.v[2]  +=  vOrtho.v[2] * speed;   

}


// Draw the robot
void Robot::drawRobot( void )
{
    
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glPushMatrix();
        glTranslatef(m_pPosition.v[0],0.80,m_pPosition.v[2]);
        glRotatef(-m_vDirection.angleSigned(Vector3(1,0,0))*_180_OVER_PI, 0.0, 1.0 ,0.0);
        glRotatef(90,0,1,0);
        glScalef(0.3,0.3,0.3); 
            //Head and BODY
            glPushMatrix();
                glPushMatrix();
                    glTranslatef(0.0,0.5,0.0);
                    glRotatef(-headAngleZ,1,0,0); 
                    glRotatef(-headAngleY,0,1,0);
                    glTranslatef(0.0,-0.5,0.0);
                    glCallList(HEAD);   
                glPopMatrix();
                glPushMatrix();
                    glCallList(BODY);   
                glPopMatrix();
                
                // RIGHT ARM, FOREARM and PALM
                glPushMatrix();
                    glTranslatef(-1.1,0.25,0);
                    glRotatef(rightArmAngle,1,0,0);
                    glTranslatef(0,-0.25,0);
                    glPushMatrix();
                        glCallList(ARM);
                    glPopMatrix();
                    
                    glPushMatrix();
                        glTranslatef(0.0,-0.7,0);
                        glRotatef(rightForearmAngle,1,0,0);	
                        glTranslatef(0.0,0.7,0);
                        glPushMatrix();
                            glCallList(FOREARM);
                        glPopMatrix();
                        glPushMatrix();
                            glTranslatef(0.0,-1.65,0);
                            glRotatef(rightPalmAngle,0,0,1);	
                            glCallList(PALM);
                        glPopMatrix();
                    glPopMatrix();
                glPopMatrix();
                
        
                // LEFT ARM, FOREARM and PALM
                glPushMatrix();
                    glTranslatef(1.1,0.25,0);
                    glRotatef(leftArmAngle,1,0,0);
                    glTranslatef(0,-0.25,0);
                    glPushMatrix();
                        glCallList(ARM);
                    glPopMatrix();
                    
                    glPushMatrix();
                        glTranslatef(0.0,-0.7,0);
                        glRotatef(leftForearmAngle,1,0,0);	
                        glTranslatef(0.0,0.7,0);
                        glPushMatrix();
                            glCallList(FOREARM);
                        glPopMatrix();
                        glPushMatrix();
                            glTranslatef(0.0,-1.65,0);
                            glRotatef(-leftPalmAngle,0,0,1);	
                            glCallList(PALM);
                        glPopMatrix();
                    glPopMatrix();
                glPopMatrix();
            glPopMatrix();
    glPopMatrix();
    glPopAttrib();
    //m_vDirection.draw(m_pPosition);    
}

// Robot rotation
void Robot::yaw(float speed)
{
    //Vector3 vView = m_vDirection - m_pPosition;    // Get the view vector   
     
    Vector3 vView(m_vDirection);

    m_vDirection.v[0] = (float)(cos(speed)*vView.v[0] - sin(speed)*vView.v[2]);   
    m_vDirection.v[2] = (float)(sin(speed)*vView.v[0] + cos(speed)*vView.v[2]);
    m_vDirection.normalize(); //Keep vector normalized

    vView = m_vHeadView;
    m_vHeadView.v[0] = (float)(cos(speed)*vView.v[0] - sin(speed)*vView.v[2]);   
    m_vHeadView.v[2] = (float)(sin(speed)*vView.v[0] + cos(speed)*vView.v[2]);
    m_vHeadView.normalize(); //Keep vector normalized

}

//Robout mouse control
void Robot::setViewByMouse(int x, int y, float sensX, float sensY)   
{   

    int middleX = glutGet(GLUT_WINDOW_WIDTH) >> 1; 
    int middleY = glutGet(GLUT_WINDOW_HEIGHT) >> 1;
    float angleY;                              
    float stepZ;                              
    static float currentRotX = 0.0f;

    if( (x == middleX) && (y == middleY) )   
        return;   

    glutWarpPointer(middleX,middleY);


    angleY = -(float)( (middleX - x) ) / sensX;          
    
    stepZ = (float)( (middleY - y) ) / sensY;          

    Vector3 vViewPrXZ(m_vHeadView.v[0], 0.0 ,m_vHeadView.v[2]);
    Vector3 vDirPrXZ(m_vDirection.v[0], 0.0 ,m_vDirection.v[2]);
    float angleYV=vViewPrXZ.angleSigned(vDirPrXZ);              // Find head view angle around Y axis
    if ((angleYV < -HEAD_Y_ANGLE_MAX)&&(angleY<0)) angleY = 0;  // Restrict movement around Y axis
    if ((angleYV > HEAD_Y_ANGLE_MAX)&&(angleY>0)) angleY = 0;   // Restrict movement around Y axis
    headAngleY = angleYV * _180_OVER_PI;                        // Update head position
    
    // Rotate view around Y axis
    Vector3 vView(m_vHeadView);
    m_vHeadView.v[0] = (float)(cos(angleY)*vView.v[0] - sin(angleY)*vView.v[2]);   
    m_vHeadView.v[2] = (float)(sin(angleY)*vView.v[0] + cos(angleY)*vView.v[2]); 
    m_vHeadView.normalize();

   
    if ((m_vHeadView.v[1] < -HEAD_Z_MAX)) m_vHeadView.v[1] = -HEAD_Z_MAX;   // Restrict movement around Z axis
    if ((m_vHeadView.v[1] > HEAD_Z_MAX)) m_vHeadView.v[1] = HEAD_Z_MAX;     // Restrict movement around Z axis

    m_vHeadView.v[1] += stepZ;
    headAngleZ = asinf(m_vHeadView.v[1]/m_vHeadView.length())* _180_OVER_PI; //Calculate head angle
}

void Robot::initStructures(void)
{
    glGenLists(12);
    structHead();
    structBody();
    structArm();
    structForearm();
    structPalm();
}

void Robot::SetMaterial(GLfloat spec[], GLfloat amb[], GLfloat diff[], GLfloat shin[])
{

  glMaterialfv(GL_FRONT, GL_SPECULAR, spec);
  glMaterialfv(GL_FRONT, GL_SHININESS, shin);
  glMaterialfv(GL_FRONT, GL_AMBIENT, amb);
  glMaterialfv(GL_FRONT, GL_DIFFUSE, diff);
}

void Robot::structHead(void)
{
    glNewList(HEAD,GL_COMPILE);
    glScalef(1.8,0.2,1.0);
    SetMaterial(mat_specularYELLOW, mat_ambientYELLOW, mat_diffuseYELLOW, mat_shininessYELLOW);
    glTranslatef(0,4.5,0);
    glScalef(0.3,2.0,0.5);
    glScalef(1.0,1.3,1.0);
    glutSolidSphere(0.5,30,30);

    SetMaterial(mat_specularBLUE, mat_ambientBLUE, mat_diffuseBLUE, mat_shininessBLUE);
    
    glTranslatef(0.0,0.2,0.2);
    glScalef(0.8,0.4,0.5);
    glutSolidCube(1.0);

    glEndList();
}

//Body display list
void Robot::structBody(void)
{
    if (!_TextureLoader.LoadTextureFromDisk("robot2.jpg",&m_BodyTexture)) std::cerr<<"Unable to load texture. Disabling."; //Load Texture
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT );
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT );	

    GLUquadricObj *g_sphere = gluNewQuadric( );             // Quadratic texturing
    gluQuadricNormals( g_sphere, ( GLenum )GLU_SMOOTH );
    gluQuadricTexture( g_sphere, GL_TRUE );


    glNewList(BODY,GL_COMPILE);
    SetMaterial(mat_specularGRAY, mat_ambientGRAY, mat_diffuseGRAY, mat_shininessBLUE);
    if( m_BodyTexture.TextureID )
    {
        glEnable( GL_TEXTURE_2D );
        glTexEnvi( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE );
        glLightModeli(GL_LIGHT_MODEL_COLOR_CONTROL,GL_SEPARATE_SPECULAR_COLOR);
        glBindTexture( GL_TEXTURE_2D, m_BodyTexture.TextureID );
    }
    glScalef(1.8,1.0,1.0);
    glPushMatrix();
        glRotatef(90.0,1,0,0);
        gluSphere(g_sphere,0.6,40,30);      //Textured body
    glPopMatrix();
    if( m_BodyTexture.TextureID ){
        glDisable( GL_TEXTURE_2D );
        glLightModeli(GL_LIGHT_MODEL_COLOR_CONTROL,GL_SINGLE_COLOR);
    }
    glTranslatef(0.0,-0.75,0.0);
    SetMaterial(mat_specularYELLOW, mat_ambientYELLOW, mat_diffuseYELLOW, mat_shininessYELLOW);
    glPushMatrix();
        glTranslatef(0.0,-0.75,0.0);
        glScalef(1,3,1);
        glutSolidCube(0.5);
    glPopMatrix();
    SetMaterial(mat_specularGRAY, mat_ambientGRAY, mat_diffuseGRAY, mat_shininessGRAY);
    glPushMatrix();
        glTranslatef(0.0,-1.5,0.0);
        glScalef(1,1,2.5);
        glutSolidCube(0.75);
    glPopMatrix();

    glTranslatef(0,0.3,0);
    SetMaterial(mat_specularGRAY, mat_ambientGRAY, mat_diffuseGRAY, mat_shininessGRAY);
    glutSolidSphere(0.5,20,20);    
    glEndList();
}

void Robot::structArm(void)
{
    glNewList(ARM,GL_COMPILE);
    SetMaterial(mat_specularGRAY, mat_ambientGRAY, mat_diffuseGRAY, mat_shininessGRAY);
    glTranslatef(0,0.25,0.0);
    glScalef(0.5,0.5,0.5);
    glutSolidSphere(0.5,20,20);

    glTranslatef(0.0,-1.10,0.0);
    glScalef(0.5,1.5,0.5);
    SetMaterial(mat_specularGRAY1, mat_ambientGRAY1, mat_diffuseGRAY1, mat_shininessGRAY1);
    glutSolidCube(1.0);

    glEndList();

}

void Robot::structForearm(void)
{
    glNewList(FOREARM,GL_COMPILE);
    

    glTranslatef(0.0,-0.7,0.0);
    glScalef(0.5,0.5,0.5);
    SetMaterial(mat_specularGRAY, mat_ambientGRAY, mat_diffuseGRAY, mat_shininessGRAY);
    glutSolidSphere(0.4,20,20);
    
    glTranslatef(0.0,-1.2,0.0);
    glScalef(0.8,2.0,1.0);
    SetMaterial(mat_specularRED, mat_ambientRED, mat_diffuseRED, mat_shininessRED);
    glutSolidCube(0.9);
    glEndList();

}

void Robot::structPalm(void)
{
    glNewList(PALM,GL_COMPILE);
    SetMaterial(mat_specularRED, mat_ambientRED, mat_diffuseRED, mat_shininessRED);
    glScalef(.2,0.5,0.7);
    glTranslatef(0.0,-0.4,0.0);
    glutSolidCube(.5);


    glTranslatef(0.0,-0.25,0.0);
    glutSolidCube(.3);
    glEndList();
}



