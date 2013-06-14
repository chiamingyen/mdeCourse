#pragma once
#ifndef ROBOT_H__
#define ROBOT_H__

#include "TextureLoader.h"
#include "Vector3.h"

class Robot
{
public:
    Robot(void);
    ~Robot(void);

    void set( float positionX, float positionY, float positionZ, float viewX, float viewY, float viewZ);

    void move(float speed);
    void strafe(float speed);	
    void setLook(void);
    void drawRobot(void);
    void setViewByMouse(int x, int y, float sensX, float sensY); 
    void yaw(float speed);
    void initStructures(void);
    void moveRightArm(float speed);
    void moveRightForearm(float speed);
    void moveLeftArm(float speed);
    void moveRightPalm(float speed);
    void moveLeftForearm(float speed);
    void moveLeftPalm(float speed);
    void moveHeadY(float speed);
    void moveHeadZ(float speed);

    float moveSpeed;
    float angleSpeed;

private:

    Vector3 m_pPosition;
    Vector3 m_vHeadView;
    Vector3 m_vDirection;
    static const float HEAD_Y_POS;
    static const float HEAD_YAW_MIN;
    static const float HEAD_Y_ANGLE_MAX;
    static const float HEAD_Z_ANGLE_MAX;
    static const float HEAD_Z_MAX;
    static const float PALM_ANGLE_MAX;
    static const float FOREARM_ANGLE_MAX;

    float headAngleY;
    float headAngleZ;
    float rightArmAngle;
    float leftArmAngle;
    float rightForearmAngle;
    float leftForearmAngle;
    float rightPalmAngle;
    float leftPalmAngle;

    void structHead(void);
    void structBody(void);
    void structArm(void);
    void structLeftArm(void);
    void structForearm(void);
    void structLeftForearm(void);
    void structPalm(void);
    void structLeftPalm(void);

    void SetMaterial(GLfloat spec[], GLfloat amb[], GLfloat diff[], GLfloat shin[]);

    TextureLoader _TextureLoader;
    glTexture m_BodyTexture;
};

#endif // ROBOT_H__
