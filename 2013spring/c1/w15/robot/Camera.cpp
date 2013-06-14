#include "Camera.h"

Camera::Camera(void)
{
    moveSpeed=0.08;
    set(0,0,0,1,0,0,0,1,0); //Default
}

Camera::~Camera(void)
{
}

Camera::Camera( float positionX, float positionY, float positionZ,   
                        float viewX,     float viewY,     float viewZ,   
                        float upVectorX, float upVectorY, float upVectorZ)
{
set(  positionX,  positionY,  positionZ,   
      viewX,      viewY,      viewZ,   
      upVectorX,  upVectorY,  upVectorZ);
}

void Camera::set( float positionX, float positionY, float positionZ,   
                  float viewX,     float viewY,     float viewZ,   
                  float upVectorX, float upVectorY, float upVectorZ)   
{   
    //  
    Vector3 Position    = Vector3(positionX, positionY, positionZ);   
    Vector3 View        = Vector3(viewX, viewY, viewZ);   
    Vector3 UpVector    = Vector3(upVectorX, upVectorY, upVectorZ);   
   
    //
    m_pPosition = Position;     
    m_pView     = View;             
    m_vUpVector = UpVector;
}

void Camera::set( Vector3 position, Vector3 view)
{   

    m_pPosition = position;     
    m_pView     = view;             
    m_vUpVector = Vector3(0,1,0);
}

//Quaternion Method for 3D Rotation
void Camera::rotateView(float angle, float x, float y, float z)   
{   
    Vector3 vNewView;   
   
       
    Vector3 vView = m_pView - m_pPosition;        
    //vView.normalize();
      
    float cosTheta = (float)cos(angle);   
    float sinTheta = (float)sin(angle);   
   
       
    vNewView.v[0]  = (cosTheta + (1 - cosTheta) * x * x)        * vView.v[0];   
    vNewView.v[0] += ((1 - cosTheta) * x * y - z * sinTheta)    * vView.v[1];   
    vNewView.v[0] += ((1 - cosTheta) * x * z + y * sinTheta)    * vView.v[2];   
   
       
    vNewView.v[1]  = ((1 - cosTheta) * x * y + z * sinTheta)    * vView.v[0];   
    vNewView.v[1] += (cosTheta + (1 - cosTheta) * y * y)        * vView.v[1];   
    vNewView.v[1] += ((1 - cosTheta) * y * z - x * sinTheta)    * vView.v[2];   
   
       
    vNewView.v[2]  = ((1 - cosTheta) * x * z - y * sinTheta)    * vView.v[0];   
    vNewView.v[2] += ((1 - cosTheta) * y * z + x * sinTheta)    * vView.v[1];   
    vNewView.v[2] += (cosTheta + (1 - cosTheta) * z * z)        * vView.v[2];   
   
      
    m_pView = m_pPosition + vNewView;   
}   

//Moves camera forward / backward
void Camera::move(float speed)
{
    Vector3 vView = m_pView - m_pPosition;    // Get the view vector   
    vView.normalize();         
       
    m_pPosition += vView * speed;
       
    m_pView += vView * speed;
         
}

void Camera::yaw(float speed)
{
    rotateView(speed, 0, 1, 0);
}

  
void Camera::strafe(float speed)   
{   
    Vector3 vStrafe = m_pView - m_pPosition;
    vStrafe = vStrafe.cross(m_vUpVector);
   
        
    vStrafe.normalize();
    
    m_pPosition += vStrafe * speed;

    m_pView += vStrafe * speed; 
} 

void Camera::pitch(float speed)
{
    rotateView(speed, 1, 0, 0);
}

void Camera::up(float speed)
{
    Vector3 vView = m_pView - m_pPosition;
    Vector3 vTemp = vView.cross(m_vUpVector);
    vTemp = vTemp.cross(vView);

    vTemp.normalize();

    m_pPosition += vTemp * speed;

    m_pView += vTemp * speed; 
}

//Mouse camera control
void Camera::setViewByMouse(int x, int y, float sensX, float sensY)   
{   
                            
    int middleX = glutGet(GLUT_WINDOW_WIDTH) >> 1; 
    int middleY = glutGet(GLUT_WINDOW_HEIGHT) >> 1;
    float angleY = 0.0f;                              
    float angleZ = 0.0f;                              
    static float currentRotX = 0.0f;
       

       

    if( (x == middleX) && (y == middleY) )   
        return;   
   
    glutWarpPointer(middleX,middleY);
       
    
    angleY = (float)( (middleX - x) ) / sensX;          
    angleZ = (float)( (middleY - y) ) / sensY;          
   
    static float lastRotX = 0.0f;      
    lastRotX = currentRotX;    


    currentRotX += angleZ;   


    if(currentRotX > 1.0f)        
    {   
        currentRotX = 1.0f;   


        if(lastRotX != 1.0f)    
        {   

            Vector3 vAxis = m_pView - m_pPosition;   
            vAxis = vAxis.cross(m_vUpVector);   
            vAxis.normalize();   


            rotateView( 1.0f - lastRotX, vAxis.v[0], vAxis.v[1], vAxis.v[2]);   
        }   
    }   

    else if(currentRotX < -1.0f)   
    {   
        currentRotX = -1.0f;   

        if(lastRotX != -1.0f)   
        {   


            Vector3 vAxis = m_pView - m_pPosition;   
            vAxis = vAxis.cross(m_vUpVector);   
            vAxis.normalize();   


            rotateView( -1.0f - lastRotX, vAxis.v[0], vAxis.v[1], vAxis.v[2]);   
        }   
    }   

    else    
    {      

        Vector3 vAxis = m_pView - m_pPosition;   
        vAxis = vAxis.cross(m_vUpVector);   
        vAxis.normalize();   


        rotateView(angleZ, vAxis.v[0], vAxis.v[1], vAxis.v[2]);     
    }  
   
    rotateView(angleY, 0, 1, 0);   
}   

void Camera::setLook(void)
{
        gluLookAt(m_pPosition.v[0], m_pPosition.v[1], m_pPosition.v[2],    
              m_pView.v[0],  m_pView.v[1],     m_pView.v[2],       
              m_vUpVector.v[0], m_vUpVector.v[1], m_vUpVector.v[2]); 
}
