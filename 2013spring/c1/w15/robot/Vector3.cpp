//Based on libdms OpenGL Toolkit http://resumbrae.com/ub/dms424_s03/libdms/


#include "Vector3.h"
#include <stdio.h>


const Vector3 Vector3::ZERO(0.0, 0.0, 0.0);
const Vector3 Vector3::X_AXIS(1.0, 0.0, 0.0);
const Vector3 Vector3::Y_AXIS(0.0, 1.0, 0.0);
const Vector3 Vector3::Z_AXIS(0.0, 0.0, 1.0);


Vector3::Vector3(void):buffer(NULL)
    {
    set(0, 0, 0);
    }


Vector3::Vector3(GLfloat x, GLfloat y, GLfloat z):buffer(NULL)
    {
    set(x, y, z);
    }


Vector3::Vector3(const GLfloat *va):buffer(NULL)
    {
    set(va[0], va[1], va[2]);
    }


Vector3::Vector3(const Vector3 &vec):buffer(NULL)
    {
    set(vec.v[0], vec.v[1], vec.v[2]);
    }


Vector3::~Vector3( void )
{
    if (buffer!=NULL) delete buffer;
}

Vector3& Vector3::operator= (const Vector3& vec)
    {
    set(vec.v[0], vec.v[1], vec.v[2]);
    return *this;
    }


void Vector3::set(GLfloat x, GLfloat y, GLfloat z)
    {
    v[0] = x;
    v[1] = y;
    v[2] = z;
    }


GLfloat& Vector3::operator[](int i)
    {
    if ((i >= 0) && (i < 3))
        return v[i];
    else if (i < 0)
        return v[0];
    else if (i > 2)
        return v[2];
    }


GLfloat Vector3::operator[](int i) const
    {
    if ((i >= 0) && (i < 3))
        return v[i];
    else if (i < 0)
        return v[0];
    else if (i > 2)
        return v[2];
    }


Vector3& Vector3::operator+=(const Vector3& vec)
    {
    v[0] += vec.v[0];
    v[1] += vec.v[1];
    v[2] += vec.v[2];
    return *this;
    }


Vector3& Vector3::operator-=(const Vector3& vec)
    {
    v[0] -= vec.v[0];
    v[1] -= vec.v[1];
    v[2] -= vec.v[2];
    return *this;
    }


Vector3& Vector3::operator*=(GLfloat s)
    {
    v[0] *= s;
    v[1] *= s;
    v[2] *= s;
    return *this;
    }


Vector3& Vector3::operator/=(GLfloat s)
    {
    v[0] /= s;
    v[1] /= s;
    v[2] /= s;
    return *this;
    }


Vector3 Vector3::operator+(const Vector3& vec) const
    {
    return Vector3(v[0]+vec.v[0], v[1]+vec.v[1], v[2]+vec.v[2]);
    }


Vector3 Vector3::operator-(const Vector3& vec) const
    {
    return Vector3(v[0]-vec.v[0], v[1]-vec.v[1], v[2]-vec.v[2]);
    }


Vector3 Vector3::operator-(void) const
    {
    return Vector3(-v[0],-v[1], -v[2]);
    }


Vector3 Vector3::operator*(GLfloat s) const
    {
    return Vector3(v[0]*s, v[1]*s, v[2]*s);
    }


Vector3 Vector3::operator/(GLfloat s) const
    {
    return Vector3(v[0]/s, v[1]/s, v[2]/s);
    }


bool Vector3::operator==(const Vector3& vec) const
    {
    return ((v[0] == vec.v[0]) &&
            (v[1] == vec.v[1]) &&
            (v[2] == vec.v[2]));
    }


bool Vector3::operator!=(const Vector3& vec) const
    {
    return ((v[0] != vec.v[0]) ||
            (v[1] != vec.v[1]) ||
            (v[2] != vec.v[2]));
    }

        
GLfloat Vector3::length(void) const
    {
    return std::sqrt(lengthSquared());
    }


GLfloat Vector3::lengthSquared(void) const
    {
    return v[0]*v[0] + v[1]*v[1] + v[2]*v[2];
    }


void Vector3::normalize(void)
    {
    float len = length();
    if (len > 0)
        {
        v[0] /= len;
        v[1] /= len;
        v[2] /= len;
        }
    }


GLfloat Vector3::dot(const Vector3& vec) const
    {
    return v[0]*vec.v[0] + v[1]*vec.v[1] + v[2]*vec.v[2];
    }


Vector3 Vector3::cross(const Vector3& vec) const
    {
    return Vector3(v[1] * vec.v[2] - v[2] * vec.v[1],
                   v[2] * vec.v[0] - v[0] * vec.v[2],
                   v[0] * vec.v[1] - v[1] * vec.v[0]);
    }


GLfloat Vector3::distance(const Vector3& vec) const
    {
    return std::sqrt(distanceSquared(vec));
    }


GLfloat Vector3::distanceSquared(const Vector3& vec) const
    {
    float dx, dy, dz;
    dx = v[0] - vec.v[0];
    dy = v[1] - vec.v[1];
    dz = v[2] - vec.v[2];
    return dx*dx + dy*dy + dz*dz;
    }

// Returns angle between two vectors in range 0-180
GLfloat Vector3::angle( const Vector3& vec ) const
{
    GLfloat result = (GLfloat)std::acos(this->dot(vec)/(vec.length() * this->length()));
    
    return result;

}

//Returns signed angle between two vectors (sign relative to Y axis) (0-360 deg)
GLfloat Vector3::angleSigned( const Vector3& vec ) const
{
    Vector3 vC=this->cross(vec);
    GLfloat angle=std::atan2(vC.length(),this->dot(vec));
    angle=vC.dot(Y_AXIS) < 0.0 ? -angle : angle;

    return angle;
    
}

//Draw vector
void Vector3::draw( const Vector3& origin ) const
{
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    glDisable(GL_LIGHTING);
    glPushMatrix();
    glColor3f(0.0,0.0,0.0);
    glBegin(GL_LINES);
        glVertex3f(origin.v[0], origin.v[1], origin.v[2]);
        glVertex3f(origin.v[0]+v[0], origin.v[1]+v[1], origin.v[2]+v[2]);
    glEnd();
    glPopMatrix();
    glPopAttrib();
}

// Returns string representation of the vector
char* Vector3::toString()
{
    buffer = new char[100];
    sprintf(buffer, "%.4g, %.4g, %.4g", v[0], v[1],v[2]); //No Buffer overflow checks !!!!
    return buffer;
}
