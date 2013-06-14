#pragma once

#ifndef CAMERA_H__
#define CAMERA_H__

#include <math.h>
#include "Vector3.h"

class Camera
{
public:
    Camera(void);
    Camera( float positionX, float positionY, float positionZ,   
                        float viewX,     float viewY,     float viewZ,   
                        float upVectorX, float upVectorY, float upVectorZ);
    ~Camera(void);
    void set( float positionX, float positionY, float positionZ,   
                        float viewX,     float viewY,     float viewZ,   
                        float upVectorX, float upVectorY, float upVectorZ);   
    void set( Vector3 position, Vector3 view);
    Vector3 getPosition() const { return m_pPosition; }
    void setPosition(const Vector3 &val) { m_pPosition = val; }

    Vector3 getView() const { return m_pView; }
    void setView(const Vector3& val) { m_pView = val; }

    void move(float speed);
    void yaw(float speed);
    void pitch(float speed);
    void strafe(float speed);
    void setLook(void);
    void rotateView(float angle, float x, float y, float z);
    void setViewByMouse(int x, int y, float sensX, float sensY); 
    void up(float speed);

    float moveSpeed;
private:
    Vector3        m_pPosition;      
    Vector3        m_pView;          
    Vector3        m_vUpVector;       
};
#endif // CAMERA_H__
